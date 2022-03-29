#Thermostat
def thermostatModel(actual, target):
    if actual < target:
        return 1
    else:
        return 0
tempOnorOff = thermostatModel(18,20)
print(tempOnorOff)

#Task1 Dice
import random
def dice(guess,roll):
    if guess == roll:
        print("correct")
    else:
        print("wrong! the number was", roll)
        user()

def user():
    userGuess = int(input("Enter a number 1-6: "))
    randRoll = random.randint(1, 6)
    dice(userGuess,randRoll)
user()


#Task 2 Thermostat
def thermostatModel(actual, target):
    if actual < target:
        return 1
    else:
        return 0

def userTemp():
    userT = int(input("Enter your desired temp: "))
    tempOnorOff = thermostatModel(userT,20)
    print(tempOnorOff)

for i in range (5):
    userTemp()
