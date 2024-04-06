#===========SELECTION SORT =================
#EXPLANATION: Selection sort works by finding the lowest item in a list and swapping it with the item that is currently in the first position
#Pass1 85 is swapped with 17
#Pass2 No swap because 24 is already the lowest
#Pass3 63 is swapped with 31
#Pass4 No swap because 45 is already the lowest
#Pass5 85 is swapped with 50 etc


myList = [85,24,63,45,17,31,96,50]
for index in range(len(myList)-1):
  print (myList)
  nextMinValue = min(myList[index + 1:])
  if nextMinValue < myList[index]:
      nextMinIndex = myList.index(nextMinValue)
      myList[nextMinIndex] = myList[index]
      myList[index]= nextMinValue
print(myList)
