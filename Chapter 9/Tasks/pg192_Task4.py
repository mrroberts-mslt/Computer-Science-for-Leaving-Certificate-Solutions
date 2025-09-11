n = int(input("Enter number of rows: "))
for i in range(1, n + 1):      # outer loop for rows
    for j in range(i):          # inner loop for stars
        print("*", end="")      # print stars on same line
    print() 


