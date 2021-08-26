#task1
def happyBday():
  print("Happy Birthday to you")

for i in range(3):
    happyBday()
    
#task2
def piVal():
  print(22/7)
  
piVal()

#task4
#An argument is the value that is sent to the function when it is called.
def myFunction1(baseNum, indexNum):
  print(baseNum ** indexNum)

myFunction1(5, 6) 

#task5
#An argument is the value that is sent to the function when it is called.


#task5
def myFunction2(num1, num2):
  if num1 > num2:
    print(num1, "is larger")
  
  elif num2 > num1:
    print(num2, "is larger")
  
  else:
    print(num1, " and ", num2, "are the same")
    
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
myFunction2(num1, num2) 
