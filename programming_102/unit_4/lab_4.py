# 102 Lab 4 11/4/2021

# Anagram Checker


print('Enter two strings and this function will determine if they are anagrams: ')


# request user input
first = input('first string: ')

# convert user input to a list
first_list = list(first)

# sort the list provided
first_list.sort()
print(first_list)

# request a second user input
second = input('second string: ')

# convert to user input to a list
second_list = list(second)

# sort the second list
second_list.sort()
print(second_list)

if first_list == second_list:
    print(f'{first} and {second} are anagrams')
else:
    print(f'{first} and {second} are not anagrams')



'''
list_name - list ('cat')

list_name.sort()

print(list_name)
'''