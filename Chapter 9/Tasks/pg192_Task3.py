rowVal = int(input("Enter number of rows: "))
colVal = int(input("Enter number of columns: "))
#outerloop will run the number of rows
#as python writes l to r then do inner loop on cols 
for rowIndex in range (rowVal):
    for colIndex in range (colVal):
        print("*", end="")
    print()
