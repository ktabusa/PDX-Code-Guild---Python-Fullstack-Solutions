# test notes for 

nums = range(0,20)

doubled_only = [num * 2 for num in nums if num % 2]

# this set of parens is not required, but it just helps to organize / show the code
doubled_evens = [(num * 2 if num %2 == 0 else num) for num in nums]
# for and in are the break statements for the comprehensions



print(doubled_only)

print(doubled_evens)

# Type errors and exception testing

while True:
    num = input("give me a number: ")
    try:
        num = int(num)
        break
    except ValueError:
        print("please enter a valid number.\n")

# https://towardsdatascience.com/all-about-python-list-comprehension-14dd979ec0d1
# https://www.programiz.com/python-programming/list-comprehension