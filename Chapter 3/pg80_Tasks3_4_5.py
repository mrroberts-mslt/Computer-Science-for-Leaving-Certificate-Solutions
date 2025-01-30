import random
#Task 1
# Open CSV file for writing
file = open("myNums.csv", mode="w")


# Generate and write 100 random integers between 0 and 100
random_numbers = []
for i in range(100):
    num = random.randint(0, 100)
    random_numbers.append(num)
    file.write(str(num)+","+"\n")

file.close()
print("CSV file 'myNums.csv' has been created successfully.")
#Task 2
#Open new CSV file for numbers over 50
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
print("CSV file 'over50.csv' has been created successfully.")

#Task 3
# Read myNums.csv, modify values greater than 30 to 30, and write to a new file
infile = open("myNums.csv", mode="r")
outfile = open("modifiedNums.csv", mode="w")
reader = infile.readlines()

for line in reader:
    num = int(line.strip())
    num = 30 if num > 30 else num
    outfile.write(str(num) + "\n")

infile.close()
outfile.close()

print("CSV file 'modifiedNums.csv' has been created successfully.")



