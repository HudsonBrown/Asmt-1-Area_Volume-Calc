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

from assertions import add2
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
        if not choice == "q" or choice == "v" or choice == "d":
            print("Sorry, that was not an option, try again. \n")
            sleep(1)
        else:
            return choice
    
def area_circle_(choice): # calculates area from radius with fomula (form)    
    form = "A = πr^2"
    while True:
        try:
            rad = float(input("Enter the radius of your circle (radius = 1/2 diameter): "))
        except:
            print('Please input an integer or floating point value.')
            time.sleep(1)
        else:
            if choice == "d":
                print(f"π * r^2 = {pi * rad^^2}")
            elif choice =="v":
                print(f"π * r^2 = {pi * rad^^2}, A = πr^2")
            else:
                print("Something went wrong")
            break

while True: #Main Program

    
    