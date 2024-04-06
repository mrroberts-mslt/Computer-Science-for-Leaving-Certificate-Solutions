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
  
  #ignore the first value and check the rest of the list for the lowest value (17)
  #on each iteration increase the index value by 1 thus ignoring each "sorted" item
  nextMinValue = min(myList[index + 1:])
  
  #if 17 is less than INDEX 0 (85) True
  if nextMinValue < myList[index]:
      
      # [85, 24, 63, 45, 17, 31, 96, 50].index(17) which returns position 4
      nextMinIndex = myList.index(nextMinValue)
      
      #move 17 from position 4 to position 0
      myList[nextMinIndex] = myList[index]
      myList[index]= nextMinValue
print(myList)



myList = [85,24,63,45,17,31,96,50]
for index in range(len(myList)-1):
  print (myList)
  nextMinValue = min(myList[index + 1:])
  if nextMinValue < myList[index]:
      nextMinIndex = myList.index(nextMinValue)
      myList[nextMinIndex] = myList[index]
      myList[index]= nextMinValue
print(myList)
