#one argument
for y in range(5):
    print (y)
    
#two arguments - first is called start argument, second id called stop argument
for y in range(1,5):
    print (y)

#three arguments - third one is known as a step argument
for y in range(1,10,2):
    print (y)

#going backwards
for y in range(10,0,-1):
    print (y)
    
'''When using the range function remember that:
All arguments must be integers
All arguments can be positive or negative
Where there is only one argument the list starts at 0..
..and lists values up to but not including y
When counting up or down in steps, you need to use a third ..
..argument to specify the increment or decrement''' 