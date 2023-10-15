'''
TPRG 2131 Fall 2023 Assignment 1
October 6th, 2023
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

After selection at level 1, the calculator expects data to entered (use appropiate data types).

'''

from time import sleep
from math import pi

def level_0_(): #To be updated
    while True:
        # for choice d, show the numbers and the product, for V show D and the formula
        choice = input("""
Enter Q/q to quit at any time;
Enter V to change the calculated view;
Enter D for default view;
Selection:
    """).lower()
        q_check_(choice)
        if choice in ["v", "d"]:
            return choice
        else:
            invalid_()
        
def level_1_(choice):
    func = {
        1: rectangular_prism_,
        2: triangular_prism_,
        3: cylinder_,
        4: rectangle,
        5: circle_
        }
    while True:
        shape = input("""
What shape would you like to calculate the area or volume for?
Enter 1, 2, 3, 4, 5, or Q/q to quit:
1. Rectangular prism
2. Triangular prism
3. Cylinder
4. Rectangle
5. Circle
        """)
        print()
        q_check_(shape)
        shape = int(shape)
        if shape in [1, 2, 3, 4, 5]:
            break
    shape = func[shape]()
    calc = shape[0]
    formula = shape[1]
    
    print(calc)
    if choice == "v":
        print(formula)

def dims_(number):
    words = {
        0 : ["radius", "height"],
        1 : ["radius"],
        2 : ["length", "width"],
        3 : ["length", "width", "height"]
        }
    while True:
        dimensions = []
        try:
            for n in words[number]:
                x = input(f"Enter the {n}: ")
                q_check_(x)
                x = int(x)
                if x <= 0:
                    raise ValueError
                else: dimensions.append(float(x))
        except ValueError:
            invalid_()
        else:
            return dimensions

def q_check_(input):
    if input in ["q", "Q"]:
        leave_()
    else:
        return

def invalid_():
    print("\nThat was not an option. Please try again.")
    sleep(1)

def rectangular_prism_():
    sides = dims_(3)
    volume = sides[0] * sides[1] * sides[2]
    calc = f"{sides[0]} * {sides[1]} * {sides[2]} = {volume} (units cubed)"
    formula = "l * w * h = V (units cubed)"
    return [calc, formula]

def triangular_prism_():
    sides = dims_(3)
    volume = sides[0] * sides[1] * sides[2] / 2
    formula = "l * w * h / 2 = V (units cubed)"
    calc = f"{sides[0]} * {sides[1]} * {sides[2]} / 2 = {volume} (units cubed)"
    return [calc, formula]

def cylinder_():
    sides = dims_(0)
    volume = round((pi * int(sides[0])**int(2) * sides[1]), 2)
    calc = f"π * {sides[0]}**2 * {sides[1]} = {volume} (units cubed)"
    formula = "{π} * r**2 * h = V (units cubed)"
    return [calc, formula]
        
def rectangle():
    sides = dims_(2)
    area = sides[0] * sides[1]
    calc = f"{sides[0]}* {sides[1]} = {area} (units squared)"
    formula = "l * w = A (units squared)"
    return [calc, formula]

def circle_():
    sides = dims_(1)
    area = round((pi * sides[0] * 2), 2)
    calc = f"2 * π * {sides[0]} = {area} (units squared)"
    formula = "2 * {π} * r (units squared)"
    return [calc, formula]

def leave_():
    print("Thank you for using this program.")
    sleep(1)
    exit()

choice = level_0_()
while True: #Main Program
    try:
        lvl_1 = None
        if lvl_1 != True:
            level_1_(choice)
            lvl_1 = True
        select = input("""
Would you like to continue?
y/n: """).lower()
        if select not in ["y", "n", "q"]:
            raise TypeError
    except TypeError:
        invalid_()
        lvl_1 = None
    else:
        if select in ["q", "n"]:
            q_check_(select)
        elif select == "y":
            lvl_1 = False