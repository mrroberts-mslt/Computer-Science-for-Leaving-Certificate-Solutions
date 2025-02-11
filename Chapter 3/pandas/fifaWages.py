import statistics
file = open("playerWages.csv","r")
dataIn = file.read()
myList = dataIn.split("\n")
myList = [int(item) for item in myList]
#quite a few players with 0 wages! lets get rid of em.
myList =[item for item in myList if item !=0]
myList.sort(reverse =True)
#myList.sort()
print("Top wages first! ", myList)

average = statistics.mean(myList)
print("Average ", average)
minimum = min(myList)
print("Minimum ", minimum)
maximum = max(myList)
print("Maximum ", maximum)

mode = statistics.mode(myList)
print("Mode ", mode)
#etc