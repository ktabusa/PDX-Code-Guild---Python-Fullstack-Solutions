# Wednesday 11/03/21 - Prog 102 Unit_03

# This is review of unit_02
# This REPL will ensure that users enter a a valid choice and will output a message according

'''
valid_yes = ['yes', 'y', 'yep']
valid_no = ['no', 'n', 'nope']

valid_choices = []
valid_choices.extend(valid_yes)
valid_choices.extend(valid_no)

while True:
    print("\nWelcome to the game!")
    # other code ...
    # ask the user if they want to play again
    again = input('Do you want to play again? y/n: ')

    # check to make sure the user has entered a valid choice, using another REPL
    # loop until the user enters a valid choice for the 'again' variable
    while again not in valid_choices:
        print("\nInvalid selection!")
        print(f"Valid choices: {', '.join(valid_choices)}") # display the choices to the user
        again = input("Please enter a valid selection: ")


    # once the code reaches this point,
    # the user is guaranteed to have entered a valid choice
    # check which list contains the user's choice
    if again in valid_yes:
        print("\nOkay, let's play again!")
    elif again in valid_no:
        print("\nGoodbye!")
        break
    # the break statement here ends the game and exits

'''

# -------------------------------------------------------------------
# Functions

# named code blocks that perform specific tasks
# take in data, manipulate it and return the result to where the function was called
# must be executed with parentheses after their name

# keyword 'def' to define a function

# variables in the parentheses in the function's definition are called 'parameters'
# parameters are empty variables, awaiting data (can also be given default values)
# note for functions if we def multiply(a,b) and then have pass in the line below, 
# we can 'skip' having any meat to the function and the print would return 'none'
'''
def multiply(a, b):
    return a * b

# define a variable using the return value from the function
product = multiply(2, 3)
print(product)

# define a variable using the sum of the return values from two function calls

product_sum = multiply(2, 10) + multiply(2, 3)
'''
# print(product_sum) # 26

# A function call is equal to its return value
# print(multiply(2, 10) == 20) # True

# 'arguments' must be passed to fill parameters if no default values are provided
# multiply() # TypeError: multiply() missing 2 required positional arguments: 'a' and 'b'

# --------------------------------------------------------

# print(punctuate('Hello', '!!!')) # Hello!!! (text='Hello', punctuation='!!!')
# print(punctuate('Goodbye')) # Goodbye. (text="Goodbye", punctuation=default)
# print(punctuate()) # Hi. (text=default, punctuation=default)
# print(punctuate(punctuation='???')) # Hi??? (text=default, punctuation='???')

# -------------------------------------------------------
'''
# Return True if the 'number' is between 'low' and 'high'. Otherwise return False.
# this function has two return statements, but will only run one or the other
def is_in_bounds(number, low, high):
    if number >= low and number <= high:
        return True
    else:
        return False


# print(is_in_bounds(5, 1, 10)) # True
# print(is_in_bounds(100, 1, 10)) # False
'''

'''
# Display different messages based on whether a number is in bounds
x = 5
low = 0
high = 10
if is_in_bounds(x, low, high): # == True: (optional)
    print(f"{x} is between {low} and {high}")
else:
    print(f"{x} is not between {low} and {high}")
'''
# ------------------------------------------------------------------------------------------- #

# End of review

# Start of Lesson 3
''' 
Dictionaries ('dict')
- one of the most powerful datatypes in Python
- can be used to store large amounts of data and make accessing that data quick and easy
- collections of key:value pairs
- keys are used to access values
- are defined using curly brackets {}
- keys and values are separated with colons
- key:value pairs are called 'items'
- items are separated with commas
'''

# blank dictionary
blank_dictionary = {}
# print(blank_dictionary, type(blank_dictionary)) # {} <class 'dict'>


# dict keys are generally strings
# dict values can be ANY datatype, including other dictionaries
# utilizing the key value pairs below, we can look up the street, which is the key value.
# this is part of the key-value pair, with the value of 123 Faux St.

address = {"street": "123 Faux St.", "city": "Portland", "state": "Oregon", "zipcode": 123456}

# print (address['street'])
print(f'{address["city"]}, {address["state"]}, {address["zipcode"]}')


## Book example for dictionaries

book = {
    'title': 'The Hobbit',
    'author': 'JRR Tolkien',
    'pages': 200
}

# print(f"The book {book['title']} has {book['pages']} pages and was written by {book['author']}")

# ----------------------------------------------------------------------------------------- #

# cannot retrieve values at non-existent keys 
# book['characters'] # KeyError: 'characters'

# add a value at the key of 'characters'
book['characters'] = ['Bilbo', 'Gandalf', 'Smaug']
# print(book['characters']) # ['Bilbo', 'Gandalf', 'Smaug']

# add a character to the list
# .append can be used to add a value to a particular key-value pair, in this case we are adding a new char (Balin) to the character key (characters)
book['characters'].append('Balin')
# print(book['characters']) # ['Bilbo', 'Gandalf', 'Smaug', 'Balin']


# dictionary methods
# Can also use dictionary specific methods like the following

# .pop(key) - remove the key:value pair at the key and return the value
pages = book.pop('pages')
# print(pages, book)

# --------------------------------------------------------------------------------------------- #

# .update(new_dict) - add the items from the new_dict to the original dictionary
new_items = {
    'pages': 200,
    'isbn_number': 3456789876598765
}

# book.update(new_items)
# print(book)

# ----------------------------------------------------------------------------------------------- #

# as of Python 3.9, we can use the 'merge' operator
# ACTION = look up the merge method manual page.

# - note this bar method is for Python 3.9 and my current version is not python 3.9? book = book | new_items

# print(book)

# ------------------------------------------------------------------------------------------------ #


# Fruit Stand

fruit_prices = {
    'apple': 2.33,
    'banana': 1.76,
    'peaches': 2.99
}

while True:
    # ask the user which fruit they want to buy
    fruit_name = input("\nPlease enter the name of the fruit you want to buy or 'done' to quit: ")

    # exit if 'done'
    if fruit_name == 'done':
        print("\nThanks for shopping!")
        break # end the loop

    # get the price of the user's fruit_name
    price_per = fruit_prices[fruit_name]

    # ask the use how many they want
    quantity = input("Enter the quantity: ")
    
    # convert the quantity to integer
    quantity = int(quantity)

    # calculate the total
    total = quantity * price_per
    
    print(f'{quantity} {fruit_name} @ ${price_per} each - ${round(total, 2)}')
