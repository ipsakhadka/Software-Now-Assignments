import string


def get_user_input(prompt): #Asking a user a valid shift value i.e., either positive or negative integer value.
   
    while True:
        val = input(prompt)
        try:
            return int(val)
        except ValueError:
            print("Only Integer Value is Accepted. Please Insert a Integer Value(..eg: -2,-1,0,1,2)")
            
def encrypt_character(char, shift1, shift2):
    """
    Encrypt a single character based on custom rules.
    Returns: encrypted character and rule number applied.
    """

    """
    Rule is applied because during encryption character can be moved from first half of alphabet to second half 
    and viceversa and while decrypting
    encrypted text cannot be exactly reversible without knowing which rule was applied.
    """
    if char.islower():
        if char in string.ascii_lowercase[:13]: #first half from a to m
            return chr((ord(char) - ord('a') + shift1 * shift2) % 26 + ord('a')), 1 #Rule 1: shift=(shift1*shift2)
            # % 26 ensures the letter stays within the range of 26 letters.
        else:  # second half from n-z
            return chr((ord(char) - ord('a') - (shift1 + shift2)) % 26 + ord('a')), 2 #Rule 2: shift=(shift1+shift2)
            
    elif char.isupper():
       if char in string.ascii_uppercase[:13]: #first half of uppercase from A to M
            return chr((ord(char) - ord('A') - shift1) % 26 + ord('A')), 3 #Rule 3 #Rule 3: shift= -shift1
       else: #second half of uppercase N-Z
            return chr((ord(char) - ord('A') + shift2 ** 2) % 26 + ord('A')), 4 #Rule 4: shift= shift2^2
           
    else:
        return char, 0  # unchanged for spaces, punctuation, numbers

def decrypt_character(char, shift1, shift2, rule):
    """
    Decrypt a single character using the exact encryption rule applied.
    """
    if rule == 1: 
        return chr((ord(char) - ord('a') - shift1 * shift2) % 26 + ord('a'))
    elif rule == 2:
        return chr((ord(char) - ord('a') + shift1 + shift2) % 26 + ord('a'))
    elif rule == 3:
        return chr((ord(char) - ord('A') + shift1) % 26 + ord('A'))
    elif rule == 4:
        return chr((ord(char) - ord('A') - shift2 ** 2) % 26 + ord('A'))
    else:
        return char  # unchanged for spaces, punctuation, numbers.

def encrypt_file(input_file, encrypted_file, rule_map_file, shift1, shift2):#Encrypt the full text file and save the encryption rules used for each character.
    
    with open(input_file, "r", encoding="utf-8") as f: #reading orginal file using utf-8.
        #utf 8 is used to correctly read and write all characters including special symbols.
        original_text = f.read()

    encrypted_text = ""
    rule_map = ""
    for char in original_text:
        encrypted_char, rule = encrypt_character(char, shift1, shift2) #encryption is done for each character
        encrypted_text += encrypted_char
        rule_map += str(rule) #store rule index for decryption

    with open(encrypted_file, "w", encoding="utf-8") as f: #encrypted text is saved.
        f.write(encrypted_text)

    with open(rule_map_file, "w", encoding="utf-8") as f: #rule map is written.
        f.write(rule_map)

    print(f"\nFile encrypted successfully! Saved as '{encrypted_file}'.")
    print(f"Rule map saved sucessfully as '{rule_map_file}'.")

def decrypt_file(encrypted_file, rule_map_file, decrypted_file, shift1, shift2):
    """Decrypt the encrypted file using the saved rule map."""
    with open(encrypted_file, "r", encoding="utf-8") as f:
        encrypted_text = f.read()

    with open(rule_map_file, "r", encoding="utf-8") as f:
        rules = [int(r) for r in f.read()] #converting rule string back to integer.

    decrypted_text = "".join( #characters are decrypted using the saved rule map and combine and stored into a single string
        decrypt_character(c, shift1, shift2, rule)
        for c, rule in zip(encrypted_text, rules)
    )

    with open(decrypted_file, "w", encoding="utf-8") as f: # decrypted text are written to the output file using UTF-8 encoding
        f.write(decrypted_text)

    print(f"\nFile decrypted successfully! Saved as '{decrypted_file}'.")

def verify_files(file1, file2):  #Check if the contents of two files; file1 and file 2 are same or not.
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
        return f1.read() == f2.read()


def main():
    print("Hello. Warm Greeting! \n")
    print("Welcome to the Text Encryption and Decryption!\n \n")
    shift1= get_user_input("Please insert a shift1:")
    shift2 =get_user_input("Enter insert a shift2:")

    encrypt_file("raw_text.txt", "encrypted_text.txt", "rule_map.txt", shift1, shift2) #Encrypting the file
    decrypt_file("encrypted_text.txt", "rule_map.txt", "decrypted_text.txt", shift1, shift2) #Decrypting the file

    if verify_files("raw_text.txt", "decrypted_text.txt"): #Verifying the decryption
        print("\nCongralution!")
        print("Success! The decrypted file matches the original file perfectly!")
        
    else:
        
        print("Sorry, something went wrong")
        print("The orginal and decrypted file did not matched. \n Please Try Again ")

if __name__ == "__main__": # Running the main program only if this file is executed directly
    main()

