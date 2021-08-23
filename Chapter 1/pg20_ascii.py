character="A"
ascii=ord(character) #ord function takes a character and returns the ASCII decimal value
print(type(ascii)) #type function prints the type of variable it is an int as it is 65
print("The decimal value for letter A is: ", ascii)

output = chr(ascii)
print(type(output))
print("The character represented by decimal value", ascii, "is: ", output)
