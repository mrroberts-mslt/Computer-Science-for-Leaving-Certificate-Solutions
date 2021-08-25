rowVal = int(input("Enter number of rows: "))

numPrinted = 0

while numPrinted <= rowVal:
    spaces = "\t"  
    print ((numPrinted + spaces) * "*")
    numPrinted += 1
    spaces +=1
