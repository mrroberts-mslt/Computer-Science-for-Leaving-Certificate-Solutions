#can you swap 2 list items e.g 85 and 24 using a temporary variable.
#change X for the list index values
#swap some other numbers
#how to swap 2 list items e.g 63 and 45
myList = [85,24,63,45,17,31,96,50]
print(myList)
temp = myList[0] #85
myList[0] = myList[1] #24
myList[1] = temp
print(myList)

myList = [85, 24, 63, 45, 17, 31, 96, 50]
print("Before:", myList)

for i in range(len(myList) - 1):  # go from 0 to second-last index
    temp = myList[i]
    myList[i] = myList[i + 1]
    myList[i + 1] = temp
    print(f"After swapping index {i} and {i+1}: {myList}")

