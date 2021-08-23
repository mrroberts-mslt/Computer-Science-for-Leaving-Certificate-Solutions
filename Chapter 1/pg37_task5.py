sentance = input("Enter a sentance: ")
letter = input(str("Enter a letter: "))
charCount = 0
for character in sentance:
    if character == letter:
        charCount+=1
print(charCount)