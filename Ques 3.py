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

        # Draw the inward dent (or an equilateral triangle pointing inside)
        #using 60 and 120 because equilateral Triangle and prev values gave weird diagrams for different values too
        pen.right(60)                       
        draw_edge(pen, part, depth - 1)       
        pen.left(120)                       
        draw_edge(pen, part, depth - 1)       
        pen.right(60)                       

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
    
    angle = 360 / sides            # it will set the exterior angle of the polygon set

    # Calculate radius of circumscribed circle so shape is centered
    radius = length / (2 * math.sin(math.pi / sides))

    #since the figure is drawing downwards
    indent_offset = length / 3  # approximate extra space for first-level indent

    # Move turtle to bottom starting point
    pen.penup()                    # Lift pen so no line is drawn
    pen.goto(-length/2, -radius + indent_offset) # start roughly center
    pen.setheading(0)              # Face right
    #pen.left(180 - (180 * (sides - 2) / (2 * sides)))  # orient correctly
    pen.pendown()                  # Put pen down to start drawing

    # Draw each side of the polygon 
    for _ in range(sides):
        draw_edge(pen, length, depth)   # Draw one edge
        pen.left(angle)                 # Turn to draw next side


def main():
    # Ask user if they want to start the program
    start = input("This program will draw a geometric pattern using Python's turtle graphics. " \
    "Do you want to start? (yes/no): ").strip().lower()

    if start not in ("yes", "y"):              
        print("Program stopped.")
        return
    
     # Now setting up the turtle screen 
     #doing this outside the loop because it gave error: turtle.terminator
    screen = turtle.Screen()           
    screen.title("Python Turtle")    
    screen.setup(800, 800)             
    screen.bgcolor("white")           

    pen = turtle.Turtle()              # This creates the turtle (pen)
    pen.speed(0)                       # This sets up Max drawing speed
    
    
#while testing I accidentally entered 400 and crashed my device hence, 
        # displaying menu  

    print("""
    Welcome to the Recursive Polygon Drawer!

    Recommended ranges:
    1. Number of sides: 0-12
    2. Side length (pixels): 50-700
    3. Recursion depth: 0-5
    """)


 # Using while loop so user can draw multiple shapes
    while True:

        try:
            sides = int(input("Enter the number of sides: "))
            length = int(input("Enter the side length (pixels): "))
            depth = int(input("Enter the recursion depth: "))

        except ValueError:

            print("Invalid input! Enter integer values only.")
            continue
 

       
        pen.clear()    # clear previous drawing
        pen.penup()
        pen.home()     # reset to center
        pen.pendown()
        pen.showturtle()

        # To draw the geometric shape 
        draw_shape(pen, sides, length, depth)

        pen.hideturtle()                   # Hide the turtle cursor
        # screen.mainloop()                  # This keep window open until closed
        #This crashed the loop to re-run hence commenting and testing

        # # Ask user if they want to build another polygon
                               
        to_cont = input("\nDo you want to draw another polygon? (yes/no): ").strip().lower()
        if to_cont in ("y", "yes"):
           continue # continue loop to draw another polygon
        elif to_cont in ("n", "no"):
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid Input. Please answer in Yes or No.")


if __name__ == "__main__":
    main()
