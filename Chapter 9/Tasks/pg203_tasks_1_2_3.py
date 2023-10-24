#task 1
def piVal():
    return(22 / 7)
    

pi = piVal()  # Store the return value of piVal function in a variable
print(pi)
radius = 10
areaCirc = (pi * radius) ** 2
print(areaCirc)

#task2
def divider(x,y):
    return (x/y)
    

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print(divider(num1,num2))

#task3
def findSpace(sentence):
    if sentence.__contains__(" "):
        spaceCount = 0
        for i in sentence:
            if i == " ":
                spaceCount +=1
        return spaceCount
    else:
        print("No spaces found")

#using a list method
def findSpace2(sentence):
    if sentence.__contains__(" "):
        lsSentence = list(sentence)  # Convert the sentence into a list
        spaceChr = " "
        return lsSentence.count(spaceChr)

    else:
        print("No spaces found")           
    
 
sentence = "The lazy fox jumped over the bed"
print(findSpace(sentence))   
print(findSpace2(sentence))

