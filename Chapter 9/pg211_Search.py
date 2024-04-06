#Searching and Sorting algorithms
#look for the key 17
#===========LINEAR SEARCH SIMPLE EXAMPLE=================
#EXPLANATION The key location is 7 because it first finds it at INDEX 4 then continues to search and then finds it at INDEX 7
myList = [85,24,63,45,17,31,96,17]
key = 17
for i in range(len(myList)):
    if myList[i] == key:
        location = i
        #print("Key found in :", [i])
print("Key location: ", location)

# What if same number is twice in the list?

#Use break to find first number then exit the loop

#===========LINEAR SEARCH REVERSE EXAMPLE=================
#Reverse the list search to print INDEX 4
#EXPLANATION The key location is 4 because it first finds it at INDEX 7 then continues to search and then finds it at INDEX 4
#len(myList)-1: This is the start parameter of the range function. Since range starts at this number and goes down to, but not including, the stop parameter, len(myList)-1 ensures the loop starts at the last index of myList. Lists in Python are zero-indexed, so the last item's index is len(myList) - 1.
#-1 (second occurrence): This is the stop parameter. In Python, range includes the start parameter but excludes the stop parameter. Here, -1 is used to ensure the loop goes down to index 0. Since range is exclusive of the stop parameter, setting it to -1 ensures that the index 0 is included in the iteration.
#-1 (third occurrence): This is the step parameter. It determines the increment (or in this case, decrement) between each i in the loop. A step of -1 means the loop will count backwards, reducing the index by 1 each time, which is useful for iterating over a list in reverse order.
myList = [85,24,63,45,17,31,96,17]
key = 17
for i in range(len(myList)-1,-1,-1):
    if myList[i] == key:
        location = i
        #print("Key found in :", [i])
print("Key location: ", location)

# What if the number is not in the list?

#===========LINEAR SEARCH IN A FUNCTION EXAMPLE (BEST PRACTICE)=================
#EXPLANATION The function is more efficient because the return part will stop the search as soon as the key is found if the key is not found it returns -1

myList = [85,24,63,45,17,31,96,17]
def linearSearch(listIn,key):
    for i in range(len(listIn)):
        if listIn[i] == key:
            return i
        #we dont put an else statement as we want to keep looping until True or (False return -1)
    return -1
        #print("Key found in :", [i])
print(linearSearch(myList,17))

#===========LINEAR SEARCH IN A FUNCTION EXAMPLE (using a while loop)================= 

def linearSearch(k, L):
    i = 0
    while i < len(L): # more?
        if L[i] == k: # match?
            return i # successful
        i = i + 1
    return i # unsuccessful

myList = [85,24,63,45,17,31,96,17]
key = int(input("Enter a target value: "))

result = linearSearch(key, myList)

if (result != len(myList)):
    print("%d found at position %d" %(key, result))
else:
    print("%d not found. Return value is %d" %(key, result))

#==============BINARY SEARCH USING A FUNCTION =====================
#EXPLANATION - Binary Search requires the list to be sorted first.
#It then takes the middle value and then only searches on the split upper or lower half
#If the key happens to be the middle value then it stops the search
#It continues to find the middle value in each split and only searches in the relevant upper or lower half until it finds the value
#

#first order it
myList = [85,24,63,45,17,31,96,17]
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

#Call the function
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
