file = open("number.csv", "r")
dataIn = file.read()
file.close()
myList = dataIn.split(",")
#only need this line if there is a blank value in the last column
#myList.remove(myList[-1])
print(myList)
#make a new List to capture the float data
floatList = []
for i in myList:
    floatList.append(float(i))
    print(i)
   

print(floatList)
