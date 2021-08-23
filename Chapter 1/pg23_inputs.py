print("Please enter your name: ")
visitor = input()

print ("Welcome to our school!")
print("We hope you enjoy your visit", visitor, " - thanks for coming!")


#can you use \t \n and ""

#another method is to join the two

visitor = input("Please enter your name: ")

#make sure your prompt is accurate and prompts for the right information
'''python always considers the user's input to be a string but you can tell
python otherwise and ask for a float or an integer etc. '''

#example
age = int(input("Please enter your age: "))
#or
age = input("Please enter your age: ")
age = int(age) #this converts the variable age to an integer
print("You are ", age, "years old!")


