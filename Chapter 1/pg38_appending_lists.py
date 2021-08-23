myList = [1,19,27,8,5,9]
print(myList)

myList.append(7)
print(myList)

myList.insert(3,13)
print(myList)

myList.remove(myList[-1])
print(myList)

print(myList.index(27))

myList.append(27)
print(myList.index(27)) #will only find the first location of the number 27
#print(myList)

'''Finding the frequesncy of a number in a database'''
'''ALT 2 N.B'''

numSought=27
freqNum=0
counter=0
while counter<len(myList):
    if myList[counter]==numSought:
        freqNum+=1
        print("Found at index: ", counter)
    counter+=1
print (numSought, "found", freqNum, "times")

