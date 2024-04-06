#=============INSERTION SORT================
#EXPLANATION
myList = [85,24,63,45,17,31,96,50]
for i in range(1, len(myList)):
  print(myList)
  itemInsert = myList[i]
  position = i
  while poistion > 0 and myList[position-1] > itemInsert:
    myList[position] = myList[position-1]
    position -=1
  myList[position] = itemInsert
print(myList)
  
