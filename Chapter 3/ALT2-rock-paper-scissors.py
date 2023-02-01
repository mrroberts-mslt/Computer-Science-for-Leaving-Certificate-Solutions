#Challenge! Convert the original RPS game below to make it computer v computer then see which result is the most likely to win? R,P, S?
#original rps code from https://realpython.com/python-rock-paper-scissors/
#Key skills: 
#Predict the outcome of the game / program below
#Change the code to make user computer generated random choice. 
#Use a for loop to run the game 100 times, 
#Append results to a csv file, 
#Read the CSV file into Python and do some statistics on the results, e.g Mode, Frequency, Total plays 

import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
