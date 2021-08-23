username = "Maureen"
counter = 0

while counter < 5:
    guess = input(str("Please enter your username: "))
    if guess!= username:
        print("ACCESS DENIED")
    elif guess==username:
        print("Welcome Maureen, please enter your password:")
    counter += 1
    
    