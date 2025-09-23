# Question 16(a)
# Examination Number:
from random import randint

def guess_game(max_guesses_allowed):

    secret_number = randint(1, 5)
    guess_count = 0
    user_guess = 0

    while (user_guess != secret_number):

        user_guess = int(input("Enter your guess: "))
        guess_count += 1   # Increase guess_count by 1
        if user_guess == secret_number:
            print("Congratulations! You win!")

print("Welcome to the guessing game!")
guess_game(3)
