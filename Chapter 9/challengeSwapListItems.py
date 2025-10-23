#can you swap 2 list items e.g 85 and 24 using a temporary variable.
#change X for the list index values
myList = [85,24,63,45,17,31,96,50]
print(myList)
temp = myList[X] #85
myList[X] = myList[X] #24
myList[X] = temp
print(myList)


myList = [85, 24, 63, 45, 17, 31, 96, 50]
print(myList)
for i in range(len(myList) - 1):  # go from 0 to second-last index
  #Put your code here
