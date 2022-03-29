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
