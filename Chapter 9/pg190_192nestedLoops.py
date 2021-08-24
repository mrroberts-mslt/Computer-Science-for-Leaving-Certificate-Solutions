#Nested loops are efficient because they use fewer lines of code.
print("*****")
print("*****")
print("*****")
print("*****")
print("*****")

# write code to display 5 cols and 5 rows

#pg191

cols = 5
for colIndex in range(cols):
  print("*", end = "")
  #end is used to stop adding a new line each time

#pg191

cols = 5
rows = 4
for rowIndex in range(rows):
  for colIndex in range(cols):
    print("*", end = "")
  #this add a new line after each row iteration
  print()

#pg192  
  
timesTable = 1
for timesTable in range(1,11):
  print(timesTable, ": Times Table")
  for i in range(1,11):
    ans = i * timesTable
    #make all the equals line up nicely
    if ans <= 90:
      print (timesTable, "X", i, "\t\t=",ans)
    else:
      print (timesTable, "X", i, "\t=",ans)
  
    
  
  
