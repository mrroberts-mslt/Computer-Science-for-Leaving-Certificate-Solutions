#finding out if a substring is present
#what is happening here

myName = "Jeremiah Jones"
print(myName.__contains__(" "))


myName = "JeremiahJones"
print(myName.__contains__(" "))

myName = "Jeremiah Jones"
spaceLoc = myName.index(" ")
print("Location of space:", spaceLoc)
