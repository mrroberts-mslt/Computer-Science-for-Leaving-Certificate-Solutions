#Task 3 Solution

sentence = input("enter a sentence: ")
counter = 0
vowelCount = 0
while counter < len(sentence):
    if sentence[counter]=="a" or sentence[counter]=="e" or sentence[counter]=="i" or sentence[counter]=="o" or sentence[counter]=="u" :
        vowelCount +=1
    counter+=1
print(vowelCount)

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
