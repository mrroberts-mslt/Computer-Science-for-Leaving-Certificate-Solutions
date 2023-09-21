#Change the values in the while loop to only allow marks between 50 and 99
#Change the error message
mark = float(input("Enter and exam mark between 0 and 100: "))
while mark <0 or mark >100:
    print ("Error, mark outside range.")
    mark = float(input("Re-enter mark: "))
print ("You entered", mark, "- well done!")

#Change the code below to make another number to finish the loop
# Can you change the code to make the letter X to finish?

num=int(input("Enter a number, 0 to finish:"))

total=num
while num!=0:
    num=int(input("Enter another number, 0 to finish:"))
    total+=num
print ("The total is: ", total)

