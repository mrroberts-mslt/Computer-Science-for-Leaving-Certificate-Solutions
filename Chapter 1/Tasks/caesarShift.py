character = input("Enter a Letter A-Z:")
key = int(input("Enter an number:"))
ascii= ord(character)
encLetter= chr(ascii+key)
print ("The Encrypted Letter is: ", encLetter)