def validateEmail(emailAddressIn): 
    if (emailAddressIn.count("@") == 1 and emailAddressIn.count(".") >= 1 and len(emailAddress) >= 8):
        return True
    else:
        return False
    
while True:
    emailAddress = input("enter your email: ")
    if (validateEmail(emailAddress)):
        print ("email check is valid")
        break
    else:
        print("email not valid")


    

