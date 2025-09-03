import turtle  
import math     

def draw_edge(pen, length, depth):
    
    """
    This function will recursively draw an edge of the polygon with inward dents.
    
    Also, the named parameters in this function refer to:
    : pen -> turtle object used for drawing
    : length -> length of the edge
    : depth -> recursion depth
    """
    
    if depth == 0:                 # (This is a base case: just draw a straight line)
        pen.forward(length)
    else:                          # Recursive case: split the edge
        part = length / 3.0        
        

        # Draw the first third part (which is straight)
        draw_edge(pen, part, depth - 1)

        # Draw the inward dent ( or an equilateral triangle pointing inside)
        pen.right(300)                       
        draw_edge(pen, part, depth - 1)       
        pen.left(240)                       
        draw_edge(pen, part, depth - 1)       
        pen.right(300)                       

        # Draw the last third part (which is also straight)
        draw_edge(pen, part, depth - 1)


def draw_shape(pen, sides, length, depth):
   
    """
    Now this function draws a the polygon with the given number of sides using draw_edge().
    And the parameter used for this funtion are:
    :pen-> turtle object
    :sides -> number of sides of the polygon
    :length -> side length
    :depth -> recursion depth
    """
    
    angle = 360 / sides            # yesley just exterior angle of the polygon set garxa

    # Calculate radius of circumscribed circle so shape is centered
    radius = length / (2 * math.sin(math.pi / sides))

    # Move turtle to bottom starting point
    pen.penup()                    # Lift pen so no line is drawn
    pen.goto(0, -radius)           # Go to bottom of polygon
    pen.setheading(0)              # Face right
    pen.pendown()                  # Put pen down to start drawing

    # Draw each side of the polygon 
    for _ in range(sides):
        draw_edge(pen, length, depth)   # Draw one edge
        pen.left(angle)                 # Turn to draw next side


def main():
    # Ask user if they want to start the program
    start = input("This program will draw a geometric pattern using Python's turtle graphics. Do you want to start? (yes/no): ").strip().lower()
    if start != "yes":              
        print("Program stopped.")
        return
    
    
 # Using while loop so user can draw multiple shapes
    while True:                    
        sides = int(input("Enter the number of sides: "))      
        length = int(input("Enter the side length (pixels): ")) 
        depth = int(input("Enter the recursion depth: "))     

        # Now setting up the turtle screen 
        screen = turtle.Screen()           
        screen.title("Python Turtle")    
        screen.setup(800, 800)             
        screen.bgcolor("white")           

        pen = turtle.Turtle()              # This creates the turtle (pen)
        pen.speed(0)                       # This sets up Max drawing speed

        # To draw the geometric shape 
        draw_shape(pen, sides, length, depth)

        pen.hideturtle()                   # Hide the turtle cursor
        screen.mainloop()                  # This keep window open until closed


        # # Ask user if they want to build another polygon
        # again = input("Do you want to build another polygon? (yes/no): ").strip().lower()
        # if again != "yes":                
        #     print("Exiting program. Goodbye!")
        #     break                         



if __name__ == "__main__":
    main()
