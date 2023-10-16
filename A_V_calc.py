'''
A_V_calc.py
TPRG 2131 Fall 2023 Assignment 1
October 6th, 2023
Hudson Brown 100900963
Updated October 14th
Updated October 15th

Project initiated with A_V_calc_starter.py starter file

A program which calculates the volume of a rectangular prism, cylinder, or triangular prism
or the area or a rectangle or circle. This program will also show the user the formula used (formatted or unformatted)
'''

from time import sleep
from math import pi

def level_0_():
    # the user selects betwen views
    while True:
        selection = input("""
Enter Q/q to quit at any time;
Enter V to change the calculated view;
Enter D for default view;
Selection: """).lower()
        q_check_(selection)
        if selection in ["v", "d"]:
            return selection
        else:
            invalid_()
        
def level_1_():
    # Provides the functionality for choosing what shape to calculate
    # and for outputting the formula and calculated values to the user
    func = {
        1: rectangular_prism,
        2: triangular_prism,
        3: cylinder,
        4: rectangle,
        5: circle
        }
    while True:
        selection = input("""
What shape would you like to calculate the area or volume for?
Enter 1, 2, 3, 4, 5, or Q/q to quit:
1. Rectangular prism
2. Triangular prism
3. Cylinder
4. Rectangle
5. Circle
: """)
        q_check_(selection)
        if selection in ["1", "2", "3", "4", "5"]:
            return func[int(selection)]
        else:
            invalid_()

def get_dims(shape):
    # Used for fetching user inputs from the calculator functions !!! not for menu selection
    words = {
        rectangular_prism : ["length", "width", "height"],
        triangular_prism : ["length", "width", "height"],
        cylinder : ["radius", "height"],
        rectangle : ["length", "width"],
        circle : ["radius"]
        }
    dimensions = []        
    for side in words[shape]:
        while True:
            try:
                dim = input(f"Enter the {side}: ")
                q_check_(dim)
                dim = float(dim)
                if dim <= 0:
                    raise ValueError #ensures the user does not input a negative number or number == 0
            except ValueError:
                invalid_()
            else:
                dimensions.append(dim)
                break
    return dimensions

def q_check_(input):
    # for use when user wants to quit, accessible to the user at all times
    if input in ["q", "Q"]:
        print("Thank you for using this program.")
        sleep(1)
        exit()
    else:
        return

def get_formula(shape, dimensions, choice):
    #generated with ChatGPT and modified by Hudson Brown on October 15th, the prompt was
    #"how to return a formula or return the formula after formatting it with the user input values"
    #this was done after also giving it the source code
    
    # Format the formula with the dimensions
    formulas = {
        rectangular_prism : "l * w * h = V (units cubed)",
        triangular_prism : "l * w * h / 2 = V (units cubed)",
        cylinder : "π * r**2 * h = V (units cubed)",
        rectangle : "l * w = A (units squared)",
        circle : "2 * π * r = A (units squared)"
        }
    formatted_formula = formulas[shape]
    if choice == True:
        for dim in dimensions:
            formatted_formula = formatted_formula.replace("l", str(dim), 1)
            formatted_formula = formatted_formula.replace("w", str(dim), 1)
            formatted_formula = formatted_formula.replace("h", str(dim), 1)
            formatted_formula = formatted_formula.replace("r", str(dim), 1)
        return formatted_formula
    else:
        return formatted_formula

def invalid_():
    # defines what to do in event of invalid input
    print("\nThat was not an option. Please try again.")
    sleep(1)
 
def rectangular_prism(length, width, height):
    #calculates and returns a volume value based on 3 arguments
    volume = round((length * width * height), 2)
    return volume

def triangular_prism(length, width, height):
    #calculates and returns a volume value based on 3 arguments
    volume = round((length * width * height / 2), 2)
    return volume

def cylinder(radius, height):
    #calculates and returns a volume value based on 2 arguments
    volume = round((pi * radius**2 * height), 2)
    return volume

def rectangle(length, width):
    #calculates and returns a area value based on 2 arguments
    area = round((length * width), 2)
    return area

def circle(radius):
    #calculates and returns a area value based on 1 arguments
    area = round((pi * radius**2), 2)
    return area

#only runs once on startup
if __name__ == "__main__":
    choice = level_0_()
    while True: #Main Program
        select = None        
        shape = level_1_()
        dimensions = get_dims(shape)
        product = (shape(*dimensions))
        formula = get_formula(shape, dimensions, True)
        print(f"{formula} = {product}")
        if choice == "v":
            formatted_formula = get_formula(shape, dimensions, False)
            print(formatted_formula)