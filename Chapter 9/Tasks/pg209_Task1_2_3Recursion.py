#more reading https://www.programiz.com/python-programming/examples/fibonacci-recursion
#Task1
def fibonacci():
  num1 = 0
  num2 = 1
  for i in range(100):
      result = num1+num2
      num1 = num2
      num2 = result
      print(result)
      
fibonacci()

#Task2

def fibRecur(n):
    if n <= 1:
        return n
    else:
        return(fibRecur(n-1) + fibRecur(n-2))

number = 100
for i in range (number):
    print(fibRecur(i))

#task 3 add up sum of natural numbers with recursion
def addUp(n):  
    if n <=1:
        return 1
    else:
        return n + addUp(n-1)
number = 5
print(addUp(number))
