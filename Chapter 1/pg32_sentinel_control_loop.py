mark = float(input("Enter and exam mark between 0 and 100: "))
while mark <0 or mark >100:
    print ("Error, mark outside range.")
    mark = float(input("Re-enter mark: "))
print ("You entered", mark, "- well done!")

num=int(input("Enter a number, 0 to finish:"))

total=num
while num!=0:
    num=int(input("Enter another number, 0 to finish:"))
    total+=num
print ("The total is: ", total)

