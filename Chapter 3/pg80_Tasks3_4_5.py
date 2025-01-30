import random
import csv

# Open CSV file for writing
file = open("myNums.csv", mode="w")

# Generate and write 100 random integers between 0 and 100
random_numbers = []
for i in range(100):
    num = random.randint(0, 100)
    random_numbers.append(num)
    file.write(str(num) + "\n")

file.close()

print("CSV file 'myNums.csv' has been created successfully.")

# Open new CSV file for numbers over 50
file = open("over50.csv", mode="w")
counter = 0
over_50 = []
for i in random_numbers:
    if i > 50:
        counter += 1
        over_50.append(i)

# Sort the list in ascending order
over_50.sort()

# Write sorted numbers to CSV file
for num in over_50:
    file.write(str(num) + "\n")

file.close()

print(counter)

# Read myNums.csv into a list
infile = open("myNums.csv", mode="r")
dataIn = infile.readlines()
infile.close()

# Convert each item to an integer
myList = []
for item in dataIn:
    myList.append(int(item.strip()))

# Replace any item greater than 30 with 30
for i in range(len(myList)):
    if myList[i] > 30:
        myList[i] = 30

# Write modified values to new CSV file
outfile = open("modifiedNums.csv", mode="w")
for num in myList:
    outfile.write(str(num) + "\n")
outfile.close()

print("CSV file 'modifiedNums.csv' has been created successfully.")
