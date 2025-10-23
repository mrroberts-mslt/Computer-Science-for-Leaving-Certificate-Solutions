#Bubble sort
#Explain bubble sort
#Add comments to each line of code
#Uncomment the print statment in line 9 what does this show?
#comment out line 9 and show the print statment in line 15 does this help ?

myList = [85,24,63,45,17,31,96,50]
for outerIndex in range(len(myList) - 1):
    #print(myList)
    for index in range(len(myList) - 1):
        if myList[index] > myList[index + 1]:
            tempValue = myList[index]
            myList[index] = myList[index+1]
            myList[index+1] = tempValue
            #print(myList)
print(myList)
  
