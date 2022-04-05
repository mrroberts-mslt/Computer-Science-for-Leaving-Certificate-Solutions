#basic no loop method 
myNums = (input("Please enter 10 number separated by commas: "))
file = open("myNumbers.csv", "w")
file.write(myNums)
    
file.close()

#with for loop!!
file = open("numbers.csv", "w")
for i in range (10):
    myNums = input("Please enter a number: ")
    file.write((myNums)+",")
    
file.close()
