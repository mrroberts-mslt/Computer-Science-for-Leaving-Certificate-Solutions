#tasksP33-34
#develop a program to add up the numbers between 1000 and 1500. use a while loop

#task1
num1 = 1000
total = 0
while (num1 < 1500):
        total = num1 + total
        num1+=1
        print(total)    
print("Val now = ",total)

#task2
counter = 0
total = 0
while counter <6:
    numbers= int(input("Enter a number: "))
    counter+=1
    total+=numbers
print ("The six numbers total: ",total, "the average is: ", total/6)

#task 3 same as user Maureen

username = input("Enter Username: ")
while username != "Maureen":
    username = input("Wrong username - re-enter username: ")
print ("Thank you ",username)

password = input("Enter Password: ")
while password != "abc123":
    password = input("Wrong password - re-enter password: ")
print ("You have now entered!")

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

#task5
counter = 0
total = 0
while TRUE:
    numbers= int(input("Enter a number: "))
    counter+=1
    total+=numbers
print ("The six numbers total: ",total, "the average is: ", total/6)
