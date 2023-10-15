'''
TPRG 2131 Fall 2023 Assignment 1
October, 2023
Hudson Brown 100900963

Project initiated with A_V_calc_starter.py starter file

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''

from time import sleep
from math import pi


def level_0_(): #To be updated
    while True:
        # for choice d, show the numbers and the product, for V show D and the formula
        choice = input("""
    Enter Q to quit;
    Enter V to change the calculated view;
    Enter D for default view;
    Selection:
    """).lower()
        if choice == "q":
            print("Thank you for using this program.")
            sleep(1)
            return False
        elif choice == "v":
            return 2
        elif choice == "d":
            return 1            
        else:
            print("Sorry, that was not an option, try again. \n")
            sleep(1)

def level_1_(choice):
    
    while True:
        try:
            shape = int(input("""
    What shape would you like to calculate the area or volume for?
    Enter 1, 2, 3, 4, or 5 for:
    1. Rectangular prism
    2. Triangular prism
    3. Cylinder
    4. Square
    5. Triangle
    """))
            if shape > 5 or shape < 1:
                raise ValueError
        except ValueError:
            print("That was not one of the options, please try again.")
            sleep(0.3)
        
        if choice == 1:
            print(rectangular_prism_(),)
        elif choice == 2:
            print 
        
        
        
        
def sides_(number):
    dimensions = []
    dim = ["length", "width", "height"]
    while True:
        try:
            if number == 0:
                dimensions.append(float(input("Enter the radius: ")))
                dimensions.append(float(input("Enter the height: ")))
            elif number == 1:
                dimensions.append(float(input("Enter the radius: ")))
            else:
                for n in number:
                    dimensions.append(float(input(f"Enter the {dim[n]}: ")))
            for x in dimensions:
                if x < 0:
                    raise ValueError
                else:
                    False
        except ValueError:
            print("The value you entered was not a positive integer or floating point, please try again.")
        
        return dimensions


def rectangular_prism_():
    sides = sides(3)
    volume = sides[1] * sides[2] * sides[3]
    return volume


def triangular_prism_():
    sides = sides(3)
    volume = sides[1] * sides[2] * sides[3] / 2
    return volume


def cylinder_():
    sides = sides(0)
    volume = sides[1] * sides[2]
    return volume
        

def prism_volume_(choice):
    dim = sides_(3)
    v = dim[1] * dim[2] * dim[3]
    return v

choice = level_0_()
while True: #Main Program
    level_1_(choice)