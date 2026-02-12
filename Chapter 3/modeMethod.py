myList = []
max_count = 0
mode = ""
for i in range(len(myList)):
    count = 0
    for j in range(len(myList)):
        if myList[i] == myList[j]:
            count += 1

    if count > max_count:
        max_count = count
        mode = myList[i]

print("The most common result (mode) is:", mode)
print("The number of", mode + "s is:", max_count)

