#example in the book
numBS = [1,-19,4,3,-5,2]
for item in numBS:
  if item < 0:
    numBS.remove(item)
print(numBS)

'''this works above fine but not if there is 2 negative numbers at the end of the list - why?
e.g
numBS = [1, -19, 4, 3, 5, -2, -13]
Final iteration:
item = -13 (negative), so this item is not removed because it is the last element 
and the loop has already finished iterating through the list.
How to fix'''
#Method 1 List comprehension
numBS = [1, -19, 4, 3, 5, -2, -13]
numBS = [item for item in numBS if item >= 0]
print(numBS)

#Method 2
numBS = [1, -19, 4, 3, 5, -2, -13]
i = 0
while i < len(numBS):
    if numBS[i] < 0:
        numBS.remove(numBS[i])
    else:
       # Only increment index when no removal happens  
      i += 1 
print(numBS)

#Method 3 recursion!
numBS = [1, -19, 4, 3, 5, -2, -13]
def removeLT():
    for i in numBS:
        if i < 0:
            numBS.remove(i)
            #call up the function again
            removeLT()
        
removeLT()        
print(numBS)

#Method 4 by Luke Power - make 2 new lists
numBS = [12, 45, 11, 78, 54, 2, -12, 10, -13, -14]
valid = []
invalid = []
print (numBS)
for i in ages:
    if i < 0:
        invalid.append(i)
    else:
        valid.append(i)
print (numBS)
print ("Valid =",valid)
print ("Invalid =",invalid)
