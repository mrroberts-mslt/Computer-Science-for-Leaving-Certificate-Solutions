def displayMenu():
    print ("\t**********************************")
    print ("\t*            Menu                *")
    print ("\t**********************************")
#optNumber is an argument and gets its value from userOpt
def menuOpt(optNumber):
    print ("\t**********************************")
    print ("\t*","Option", optNumber)
    print ("\t**********************************")

displayMenu()

userOpt = int(input("Enter your option : "))
menuOpt(userOpt)
# if userOpt == 1:
#     menuOpt(userOpt)
# else:
#     menuOpt(userOpt)
