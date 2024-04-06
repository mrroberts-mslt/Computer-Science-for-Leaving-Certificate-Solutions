#=============INSERTION SORT================
#EXPLANATION look at the value next to index and move it to the left if its lower
# Ignore the sorted items then move to the next value
#Pass 1: 24(index1) is less than 85(index0) so its inserted into position 0
# 24,85,63
#Pass 2: so 85 > 63 and 24 > 63 False 
# So insert 63 between the 2
# 24,63,85
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
  
