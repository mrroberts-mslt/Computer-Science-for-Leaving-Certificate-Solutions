def fibonacci():
  term1 = 0
  term2 = 1
  count = 0
  for i in range(8):
      result = term1+term2
      term1 = term2
      term2 = result
      print(result)
      
fibonacci()
