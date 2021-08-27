#Task1
def fibonacci():
  term1 = 0
  term2 = 1
  count = 0
  for i in range(100):
      result = term1+term2
      term1 = term2
      term2 = result
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
