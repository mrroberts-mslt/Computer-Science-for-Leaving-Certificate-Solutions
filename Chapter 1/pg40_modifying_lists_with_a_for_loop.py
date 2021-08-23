#why does this not work?
myList=[1,-19,27,8,-5,9]
print(myList)
for item in myList:
    if item<0:
        item=0
print(myList)

myList=[1,-19,27,8,-5,9]
print(myList)
for counter in range (len(myList)):
    if myList[counter]<0:
        myList[counter]=0
print(myList)

