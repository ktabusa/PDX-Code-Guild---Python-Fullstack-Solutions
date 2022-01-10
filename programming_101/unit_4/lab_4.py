# Lab 4 10/28/2021

# Rock Paper Scissors

# import the random module for the random.choice() fxn.  randomly selects an option from a list provided
import random 

# intro text with a loop, and the request for user input
options = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock, Paper, Scissors! (These are case sensitive by the way)\n")
print("Your options are:\n")
for option in options:
    print(f" - {option}\n")

player = input("what is your selection? ")
print(f"Player chooses {player}.")

comp = random.choice(options)
print(f"Computer chooses {comp}.")

# Extra Challenge 1
if player == comp:
    print("Tie.")

if player == "Rock" and comp == "Paper":
    print("Player loses.")

if player == "Rock" and comp == "Scissors":
    print("Player wins.")

if player == "Paper" and comp == "Scissors":
    print("Player loses.")

if player == "Paper" and comp == "Rock":
    print("Player wins.")

if player == "Scissors" and comp == "Rock":
    print("Player loses.")

if player == "Scissors" and comp == "Paper":
    print("Player wins.")
