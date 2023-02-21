#See Question: https://studyclixsaielive.azureedge.net/cms/media/papers/3dac5f7f-6941-44d9-946b-164ad772e46f.pdf
squared_numbers = []
counter = 1
for i in range (20):
    squared = counter * counter
    squared_numbers.append(squared)
    counter+=1
print(squared_numbers)

myNumber = int(input("Which squared number would you like to see? 1-20: "))
print(squared_numbers[myNumber-1])
