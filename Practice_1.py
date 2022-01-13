#Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

import pytest

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True

# Ones Digit
# Write a function that returns the ones digit of a number
def ones_digit(num):
    ones = num % 10
    return ones

def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2


# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer
def percentage(v, max):
    percent = (v / max) * 100
    rounded = round(percent, 0)
    rounded = int(rounded)
    rounded = str(rounded)
    return (rounded + '%')

def test_percentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'
