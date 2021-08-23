myString ="Frank Lampey"
print(myString)
myStringList = list(myString)
print(myStringList)

myList = [27,33,9,27,8,5,27]
numSought = 27
freqNum = 0
counter = 0
while counter < len(myList):
    if myList[counter] == numSought:
        freqNum+=1
        print("Found at index: ",counter)
    counter+=1
print (numSought, "found", freqNum,"times")

myList = [27,33,9,27,8,5,27]
numSought = 27
freqNum = 0
counter = 0
for counter in range (len(myList)):
    #counter is the iteration variable
    if myList[counter] == numSought:
        freqNum+=1
        print("Found at index: ",counter)
    counter+=1
print (numSought, "found", freqNum,"times")

myList = [1,-19,9,27,8,-5,9]
print(myList)
for counter in myList:
    if counter < 0:
        counter = 0
print(myList)

myList = [1,-19,9,27,8,-5,9]
print(myList)
for counter in range(len(myList)):
    if myList[counter] <0:
        myList[counter] = 0
print(myList)

friends = ["Joe", "Phillip", "Zara", "Frank Lampey"]
for friend in friends:
    print("Happy New Year", friend)

friends = ["Joe", "Phillip", "Zara", "Frank Lampey"]
for i in range(len(friends)):
    friend = friends[i]
    print("Happy New Year", friend)
    
friends = ["Joe", "Phillip", "Zara", "Frank Lampey"]
for i in range(1,3):
    friend = friends[i]
    print("Happy New Year", friend)
    
    
    
    
    