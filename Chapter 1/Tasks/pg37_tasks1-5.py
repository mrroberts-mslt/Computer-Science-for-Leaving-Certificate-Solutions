#Task 1
for i in range(1,11):
    print(i)

number = 0
while number <=10:
    print(number)
    number+=1

#Task 2
enterNum = int(input("Enter a number: "))
enterNum+=1
for i in range(1,enterNum,2):
    print(i)

    
#Task 3 Solution

sentence = input("enter a sentence: ")
counter = 0
vowelCount = 0
while counter < len(sentence):
    if sentence[counter]=="a" or sentence[counter]=="e" or sentence[counter]=="i" or sentence[counter]=="o" or sentence[counter]=="u" :
        vowelCount +=1
    counter+=1
print(vowelCount)


#Task 4
myPhrase = input("Enter a sentence to reverse: ")
reversePhrase=""
for i in myPhrase:
    reversePhrase = i + reversePhrase
print(reversePhrase)

#Task5
sentence = input("Enter a sentence: ")
letter = input(str("Enter a letter: "))
charCount = 0
for character in sentence:
    if character == letter:
        charCount+=1
print(charCount)

#Task 5
mySent = input("Yes enter something else please: ")
char = input("Enter a single Char: ")
count=0
charCount = 0
while count < len(mySent):
    if mySent[count] == char:
        charCount+=1
    count+=1
print(char,"Found", charCount, "Times")





#Task 3 using a list
sentence = input("enter a sentence: ")
counter = 0
vowelCount = 0
vowelList=[]
while counter < len(sentence):
    if sentence[counter]=="a" or sentence[counter]=="e" or sentence[counter]=="i" or sentence[counter]=="o" or sentence[counter]=="u" :
        vowelCount +=1
        vowelList.append(sentence[counter])
    counter+=1
print(vowelCount)
print (vowelList)

#Task 3 using a vowel list
sentence = input("Enter a sentence 3: ")
counter = 0
vowelCount = 0
vowelList=["a","e","i","o","u"]
while counter < len(sentence):
    if sentence[counter] in vowelList :
        vowelCount+=1
        print(sentence[counter])
    counter+=1
print(vowelCount)

#end
