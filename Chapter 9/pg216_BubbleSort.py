myList = [85,24,63,45,17,31,96,50]
for outerIndex in range(len(myList) - 1):
  print(myList)
  for index in range(len(myList) - 1):
    if myList[index] > myList[index + 1]:
      tempValue = myList[index]
      myList[index] = myList[index+1]
      myList[index+1] = tempValue
  print(myList)
  
