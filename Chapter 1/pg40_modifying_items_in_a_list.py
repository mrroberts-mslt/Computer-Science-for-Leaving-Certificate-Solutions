myList=[1,-19,27,8,-5,9]
print(myList)
counter=0
while counter<len(myList):
    if myList[counter]<0:
        myList[counter]=0
    counter+=1
print(myList)

#using for loops with lists
myList=[1,-19,27,8,-5,9]
print(myList)
for item in myList:
    print(item)