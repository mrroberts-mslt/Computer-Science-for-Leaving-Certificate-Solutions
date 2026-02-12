#correct version 1
myList = [3,4,5,7,4,2

max_count = 0
mode = ""

for i in range(len(myList)):
    count = 0

    for j in range(len(myList))
        if myList[i] == myList[j]:
            count += 1

    if count > max_count
        max_count = count
        mode = myList[i

print("The most common result (mode) is:", mode)
print("The number of", mode, "s is:", max_count))

#Correct version 2
myList = [3,4,5,7,4,2]

max_count = 0
mode = ""

for i in range(len(myList)):
    count = 1   # ERROR 1

    for j in range(len(myList) - 1):   # ERROR 2
        if myList[i] = myList[j]:      # ERROR 3
            count = count + 1

    if count >= max_count:   # ERROR 4
        max_count = count
        mode == myList[i]    # ERROR 5

print("The most common result (mode) is:", mode)
print("The number of", mode, "s is:", max_count + 1)  # ERROR 6
