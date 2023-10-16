"""
A_V_calc_test.py
Created by Hudson Brown, 100900963
ChatGPT was used on October 15th
prompt was to generate a pytest file based on this source code: {insert A_V_calc.py source code}
ChatGPT generated line 15 to line 35 (minus the comments)
All other code was typed by hand (with reference to this generated code)

A program to test the functionality of A_V_calc.py
"""

from A_V_calc import rectangular_prism, triangular_prism, cylinder, rectangle, circle
from math import pi
import pytest

# Defines the input values + the expected result for pytest to refer to
@pytest.mark.parametrize(
    "length, width, height, expected",
    [(2, 3, 4, 24), (5, 5, 5, 125), (0, 0, 0, 0), (-1, 2, 3, -6)],
)
#calls the calculator function with the input values and compares to the expected output value
def test_rectangular_prism(length, width, height, expected):
    result = rectangular_prism(length, width, height)
    assert result == expected

@pytest.mark.parametrize(
    "length, width, height, expected",
    [(2, 3, 4, 12), (5, 5, 5, 62.5), (0, 0, 0, 0), (-1, 2, 3, -3)],
)
def test_triangular_prism(length, width, height, expected):
    result = triangular_prism(length, width, height)
    assert result == expected

@pytest.mark.parametrize("radius, height, expected", [(2, 3, 37.7), (5, 5, 392.7), (0, 0, 0), (0, 2, 0)])
def test_cylinder(radius, height, expected):
    result = cylinder(radius, height)
    assert result == expected

@pytest.mark.parametrize("length, width, expected", [(2, 3, 6), (5, 5, 25), (0, 0, 0), (0, 2, 0)])
def test_rectangle(length, width, expected):
    result = rectangle(length, width)
    assert result == expected
    
@pytest.mark.parametrize("radius, expected", [(2, 12.57), (5, 78.54), (0, 0), (100, 31415.93)])
def test_circle(radius, expected):
    result = circle(radius)
    assert result == expected


