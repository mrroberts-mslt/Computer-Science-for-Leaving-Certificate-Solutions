#Aim is to produce a table of values giving price per square metre.
price = 45.20
print("\tWidth")
# lets make the the top part of the table, last value in the range is the step e.g increase by 5
for tableHead in range(0,25, 5):
  #using a conditional to put Length in "cell a1"!
  if tableHead == 0:
    print("Length\t", end="")
  else:
    # had to fiddle around with tabs \t to get the spacing
    print(tableHead,"m\t\t", end="")
print()

#this section does the calculation. 
#first specify the range and increment 10m to 100m (110) with increment of 10
for rowIndex in range(10, 110, 10):
  # This is to do the multiplication part e.g 10*5
  for colIndex in range(5,25, 5):
    ans=price * (colIndex * rowIndex)
    #make it sensible and readable
    ans=round(ans,2)
    print(rowIndex,"m\t", ans, end="")
  print()
  
  
  
