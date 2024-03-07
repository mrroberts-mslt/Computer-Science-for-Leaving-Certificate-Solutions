import matplotlib.pyplot as plt
file = open("myFirstCSVFile.csv", "r")
dataIn = file.read()
file.close()
#printed as a string
print(dataIn)

#creates a list from from the string by taking the delimiter (the comma in this instance) as an argument
myList = dataIn.split(",")

#printed as a list with each item as a string
print(myList)

#list comprehension
myList = [int(i) for i in myList]
'''List comprehension iterates through myList and changes each item to an integer
looks like a self contained for loop requires a square bracket
the word i is a variable and needs to be the same in both locations...does not need to be "i" '''

#the final list with each item as an int
print(myList)

plt.plot(myList)
plt.show()
