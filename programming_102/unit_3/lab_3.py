# 102 Lab 3 11/3/2021

# Unit Converter

## Version 1
## Ask the user for the number of feet, and print out the equivalent distance in meters.
## Hint: 1 ft is 0.3048 m

# V1 Prompt Title
print('Unit Converter Version 1')

# creating a dictionary to house all of our conversion factors
conversions  = {"feet": 0.3048, } 

# ask for user input
ask = input("What is the distance in feet: ")

# cast the integer variable 'feet' to a float so it can be used with the floats in the dict conversion
converted = float(ask) * conversions['feet']

# had to round the result to get the 3 decimals in the example
result = round(converted, 4)

print(f'{ask} ft is {result}\n')

# ---------------------------------------------------------------- #

## Version 2
## Allow the user to also enter the units.  The depending on the units, convert the distance in to meters.
## The units we'll allow are feet, miles, meters, and kilometers.

print("Unit Converter Version 2")

# add additional conversions to our dictionary - miles, meters, km
new_items = {'mi': 1609.34, 'm': 1, 'km': 1000}
conversions.update(new_items)

# ask the user for input
distance = input("What is the distance? ")
units = input("What are the units? ")

# multiply the distance by the dictionary value associated with the key (units)
converted_v2 = float(distance) * conversions[units]
result = round(converted_v2, 4)

print(f'{distance} {units} is {result} m')

## Version 3 
## this would improve the program to support yards and inches
imperial_items = {'yard': 0.9144, 'in': 0.0254,}
conversions.update(new_items)










# Oops - Created a function to convert the numbers - I kept this here for my own placeholder
'''
feet = input("What is the distance in feet: ")
def feet_m(feet):
    return round(float(feet) * 0.3048, 4)
    

print(f'{feet} feet is {feet_m(feet)} m')
'''