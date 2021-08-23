#name = input("Please enter your name: ")
file = open("myName.txt" , "w")
file.write(input("Please enter your name: "))
file.close()