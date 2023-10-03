#Aim is to produce a table of values giving price per square metre.

price = float(input("Enter Price per sq m: "))
print("\tWidth")

# Print the table header
# lets make the the top part of the table, last value in the range is the step e.g increase by 5
for tableHead in range(0, 25, 5):
    if tableHead == 0:
        print("Length\t", end="")
    else:
        print(tableHead, "m\t\t", end="")
print()

# Generate the table
#first specify the range and increment 10m to 100m (110) with increment of 10
for rowIndex in range(10, 110, 10):
    # Print the rowIndex in the first column and add an "m"
    print(rowIndex,"m", "\t", end="")
      # This is to do the multiplication part e.g 10*5
    for colIndex in range(5, 25, 5):
        ans = price * (colIndex * rowIndex)
        ans = int(ans)
        print("€",ans, end="\t\t")  # Separate other columns with double tabs
    print()  # Start a new row
  
  
  
