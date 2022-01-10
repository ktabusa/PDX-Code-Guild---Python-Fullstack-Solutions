# Lab 5 10/28/2021

# Password Generator

import random
import string

# defining the variables our random selector will choose a character from
letters = string.ascii_letters
digits = string.digits
punct = string.punctuation
options = letters + digits + punct

# define an empty list to append the randomly selected password characters to create the pw
password = ""

# for loop randomly choose a character while our password is below the target length
while len(password) < 10:
    new = random.choice(options)
    password + new


print(password)

"""
# print each character in the list as a string
i = 0
while i < 10:
    print(password[i])
    i += 1
"""
