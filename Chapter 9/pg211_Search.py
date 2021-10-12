#Searching and Sorting algorithms
myList = [85,24,63,45,17,31,96,50]
#print(myList[4])
#print(len(myList))
#look for the key 17

key = 17
for i in range(len(myList)):
    if myList[i] == key:
        location = i
        #print("Key found in :", [i])
print("Key location: ", location)

# What if same number is twice in the list?
#Use break to find first number then exit the loop
# What if the number is not in the list?
#        location = False


#Linear Search in function
def linearSearch(listIn,key):
    for i in range(len(listIn)):
        if listIn[i] == key:
            return i
        #we dont put an else statement as we want to keep looping until True or (False return -1)
    return -1
        #print("Key found in :", [i])
print(linearSearch(myList,17))

#Linear search example 2

def linearSearch(v, L):
    i = 0
    while i < len(L): # more?
        if L[i] == v: # match?
            return i # successful
        i = i + 1
    return i # unsuccessful

keys = [15, 4, 41, 13, 24, 14, 12, 21]
argument = int(input("Enter a target value: "))

result = linearSearch(argument, keys)

if (result != len(keys)):
    print("%d found at position %d" %(argument, result))
else:
    print("%d not found. Return value is %d" %(argument, result))

######################binary search##########################

#first order it
myList.sort()


def binarySearch(listIn, key):
    first = 0
    last = len(listIn)-1
    while (last - first) >=0:
        #get the position of the middle item in the list (should be 3) as floor division gives the lowest whole number
        middle = first + ((last - first)//2)
        #check if this is the value
        if listIn[middle] == key:
            return middle
        #if the key is less than middle value set the last value to 1 position below middle
        elif key < listIn[middle]:
            last = middle - 1
        #if the key is more than middle value set the last value to 1 position more than middle
        else:
            first = middle +1
    return -1

print(binarySearch(myList,31))

#Binary Search 2
def binary_search(v, L):
#set the lowest index
    low = 0
#set the highest index -1
    high = len(L)-1

    while (low <= high):
#floor divide to get a int
        mid = (low+high)//2
#check if the value (14) at position mid (7) is equal to v
        if L[mid] == v:
            return mid
        elif L[mid] < v:
            low = mid + 1
        else:
            high = mid - 1

    return len(L)
# Driver code ...
keys = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
argument = int(input("Enter a target value: "))

result = binary_search(argument, keys)
#check if result is not equal to 15 then the key has been found
if (result != len(keys)):
    print("%d found at position %d" %(argument, result))
else:
    print("%d not found. Return value is %d" %(argument, result))
