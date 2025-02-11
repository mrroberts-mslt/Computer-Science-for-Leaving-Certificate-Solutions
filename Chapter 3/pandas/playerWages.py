import statistics
import matplotlib.pyplot as plt
file = open("playerWages.csv","r")
dataIn = file.read()
myList=dataIn.split("\n")
#print(myList)
myList = [int(item) for item in myList]
myList= [item for item in myList if item !=0]
myList.sort(reverse=True)
print(myList)
plt.plot(myList)
plt.show()
