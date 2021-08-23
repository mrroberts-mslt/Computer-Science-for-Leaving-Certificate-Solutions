sentance = input("Enter a sentance: ")
spaceCount = 0
counter = 0
while counter < len(sentance):
    if sentance[counter]==" ":
        spaceCount+=1
    counter+=1
wordCount = spaceCount+1
print("Spaces: ", spaceCount)
print("Words: ", wordCount)


#worth stepping into to see what is going on
#square brackets...index position