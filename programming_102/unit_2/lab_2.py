# 102 Lab 2 11/1/2021

# Functions

#defining our list of numbers, with an expected sum of 53.
numbers = [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]
# Sum lab section 2.1

# we want to create a new sum function that takes input from a list of numbers and return the sum of the list.

def add_lab(numbers):
    total = 0
    # loop through the list i times to add the number in list position i to the total.
    for num in (numbers):
        total = total + num
    return total

result = add_lab(numbers)

# print the result of the function itself
print('Section 2.1 result: ')
print(result)



# Sum lab section 2.2
# print the list of numbers for the user to input for 2.2
print('\nFor section 2.2 you will enter a list of numbers and this function will sum them.')


# create an empty list to save all of our user inputs
numbers = []

# ask the user for an input
user = 0

while user != 'done':
    user = input("Enter a number or 'done' to quit: ")
    if user != 'done':
        numbers.append(int(user))

print(f'You entered {numbers}\n')
print(f'The sum of the numbers is {add_lab(numbers)}')



"""
These are test notes to see if i can similarly through a string with a for loop
string = 'abcdefgh'

def print_string():
    total = ''
    for str in (string):
        total = total + str
    return total

result = print_string()
print(result)
""" 