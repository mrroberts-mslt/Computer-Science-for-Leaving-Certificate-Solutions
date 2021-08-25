rowVal = int(input("Enter number of rows: "))
rowVal +=1

for index in range (rowVal):
    for stars in range (rowVal):
        space = rowVal * " "
        print(space, stars * "*")
        rowVal-=1
    print()
