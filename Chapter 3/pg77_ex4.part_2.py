#Needs correcting or use list comprehension
file = open("numbers.csv", "r")
dataIn = file.read()
file.close()
myList = dataIn.split(",")
print (len(myList))
myList = []
for i in range(len(myList)):
    i = float(i)
    myList.append(i)
print(myList)
