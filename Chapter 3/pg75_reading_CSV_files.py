file = open("myFirstCSVFile.csv", "r")
dataIn = file.read()
file.close()
print(dataIn) #printed as a string

myList = dataIn.split(",")
#creates a list from from the string by taking the delimiter (the comma in this instance) as an argument
print(myList) #printed as a list with each item as a string

myList = [int(item) for item in myList] #known as list comprehension
#iterates through myList and changes each item to an integer
#looks like a self contained for loop
#requires a square bracket
#the word item is a variable and needs to be the same in both locations...does not need to be "item"
print(myList)

