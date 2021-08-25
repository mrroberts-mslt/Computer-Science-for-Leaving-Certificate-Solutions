rowVal = int(input("Enter number of rows: "))

for index in range (rowVal):
    for stars in range (rowVal):
        space = rowVal * " "
        print(space, stars * "*")
        rowVal-=1
    print()
