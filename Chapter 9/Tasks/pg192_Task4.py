rowVal = int(input("Enter number of rows: "))

numPrinted = 0

while numPrinted <= rowVal:
    print("*" * numPrinted)
    numPrinted += 1

#Right Aligned


rowVal = int(input("Enter number of rows: "))

numPrinted = 1

while numPrinted <= rowVal:
    line = '*' * numPrinted  # Create a string of asterisks
    print(line.rjust(rowVal))  # Right-align the string within a field of width 'rowVal'
    numPrinted += 1


