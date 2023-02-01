#ALT2 Sample solution 
#Challenge convert the original RPS game to make it computer v computer then see which result is the most likely to win? R,P, S?
#Key skills: Change the code to make user computer generated random choice. 
#Use a for loop to run the game 100 times, 
#Append results to a csv file, 
#Read the CSV file into Python and do some statistics on the results 
#original rps code from https://realpython.com/python-rock-paper-scissors/

import random
import statistics

for i in range(100):
    file = open("rps.csv","a")
    possible_actions = ["rock", "paper", "scissors"]
    user_action = random.choice(possible_actions)
    computer_action = random.choice(possible_actions)
    print(f"\nUser chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        file.write("Draw,")
        
        
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            file.write("Rock,")

        else:
            print("Paper covers rock! You lose.")
            
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            file.write("Paper,")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            file.write("Scissors,")
        
        else:
            print("Rock smashes scissors! You lose.")
    file.close()

file = open("rps.csv","r")
dataIn = file.read()
rpsList = dataIn.split(",")
mode = statistics.mode(rpsList)
print(f"The most common result (mode) is: {mode}")
freq = rpsList.count(mode)
print(f"The number of {mode}s is: {freq}")
rockCount = 0
paperCount = 0
scissorCount = 0
drawCount = 0
for i in rpsList:
    if i == "Rock":
        rockCount+=1
    elif i == "Paper":
        paperCount+=1
    elif i == "Scissors":
        scissorCount+=1
    else:
        drawCount +=1
print("Rock = ", rockCount)
print("Paper = ", paperCount)
print("Scissors = ", scissorCount)
print("Draw = ", drawCount)
print("Total plays: ",rockCount+paperCount+scissorCount+drawCount)
