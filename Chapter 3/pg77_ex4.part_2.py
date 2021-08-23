file = open("myNumbers.csv", "r")
dataIn = file.read()
file.close()
print(dataIn) #printed as a string