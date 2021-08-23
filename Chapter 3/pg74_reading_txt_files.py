file = open("myFirstTextFile.txt", "r")
#opens the file
dataIn = file.read()
#reads the contents of the file and stores it in the variable "dataIn"
file.close()
#closes the file
print(dataIn)
#prints the contents of the file