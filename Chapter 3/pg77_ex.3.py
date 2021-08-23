passCheck = input("Please enter your password: ")
file = open("password.txt", "r")
dataIn = file.read()

if passCheck == dataIn:
    print("Entry successful")
else:
    print("Access denied")