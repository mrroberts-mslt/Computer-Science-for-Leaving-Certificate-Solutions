#finding the length of a string

string1 = "Hello"
length = len(string1)
print(length)
print(type(length))

#can you figure out what is happening here?
myString = "Frank Lampey"
print(myString [11])
print(myString [-1])
print(myString[6:10])
print(myString[-6:-2])
print(myString[:5])
print(myString[6:])
print(myString[len(myString)-1]) #why does this return the last letter?