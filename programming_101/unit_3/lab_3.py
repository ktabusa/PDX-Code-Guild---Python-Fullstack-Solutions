# Lab 3 10/28/2021

# Grading 

# import random module. Question: is it standard to include at the top as a 'header'
import random

# user inputs score, and the program checks to see if 0-100
score = int(input("Provide course score: "))
if score > 100:
    print("Invalid score provided.")
elif score >= 90:
    print("Letter grade is an A.")
elif score >= 80:
    print("Letter grade is a B.")
elif score >= 70:
    print("Letter grade is a C.")
elif score >= 60:
    print("Letter grade is a D.")
elif score >= 0:
    print("Letter grade is a F.")
else:
    print("Invalid score provided.")

# place holder for the rival comparison part teamrocket = int(randint(0, 100))

