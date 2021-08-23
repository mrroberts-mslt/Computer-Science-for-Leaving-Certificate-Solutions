inputText = "John28"
for character in inputText:
    print(character)
    
#character is just a variable name not a keyword
    
sentance = input("Enter a sentance: ")
spaceCount = 0
for character in sentance:
    if character == " ":
        spaceCount+=1
wordCount = spaceCount +1
print("Spaces: ", spaceCount)
print("Words: ", wordCount)