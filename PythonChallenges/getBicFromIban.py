#1 Allow a user to insert following IBAN as string IE95 IPBS 990711 16942378
##Use String Methods
#2 Remove space from the IBAN
#3 Check if the IBAN is alphanumeric if it is allow iban checker to proceed:
#4 Count the length of the IBAN check its 22 characters print error if its not
#5 Create a variable called BIC allow user to enter the following BIC: "IPBSIE2D"
#6 Convert the IBAN and BIC strings to Lists
#7 Get the first 4 items of the BIC List (IPBS) and assign it as a variable
#8 Get the IPBS portion of the IBAN from the List and assign it as a variable
#9 Check if the new shorter BIC and shorter IBAN Lists match print Match or No match
#10 Add some comments to your code
























#Solution
iban = insert("Enter this IE95 IPBS 990711 16942378 :")
iban = iban.replace(" ","")
if iban.isalnum():
    print("True")
    if (len(iban) !=22):
        print("Error")
    else:
        bic = insert("Enter this BIC IPBSIE2D: ")
        bicList = list(bic)
        bicList = bicList[:4]
        ibanList = list(iban)
        ibanList = ibanList[4:8]
        if (bicList == ibanList):
            print("match")
        else:
            print("No")
        
else:
    print("IBAN is misconfigured")
