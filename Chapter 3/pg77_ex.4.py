myNums = (input("Please enter 10 number separated by commas: "))
file = open("myNumbers.csv", "w")
file.write(myNums)
    
file.close()