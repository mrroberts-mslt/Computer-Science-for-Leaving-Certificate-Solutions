price = 45.20
#loop the columns first
# last value in the range is the step e.g increase by 10
for colIndex in range(0,30, 5):
  if colIndex == 0:
    print("Length ", end="")
  else:
    print(colIndex,"m\t", end="")
for rowIndex in range(0, 100, 10):
  print(rowIndex,"m\n")
  
