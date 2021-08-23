#task4
'''formula for odd numbers is 2n-1'''
numX = int(input("Enter a large number : "))
calc=0
n=1
total = 0
while total < numX:
    calc = 2*n-1
    total+=calc
    n+=1
print("Sum of odd numbers = ",total)