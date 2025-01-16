#Step 1 make 2 empty lists
salespeople = []
sales = []
numSalespeople = int(input("Enter the number of salespeople: "))

# Step 2: Collect data for each salesperson

for i in range(numSalespeople):

    name = input("Enter salesperson's name: ")
    sale = float(input("Enter total sales for" + name + " (in EUR): "))
    salespeople.append(name)
    sales.append(sale)
   
# Step 3: Save the updated data to CSV files

namesFile = open("salespeople_names.csv", "w")

for i in salespeople:
    #ensures the CSV data is written in col not row
    namesFile.write(i + "\n")
    
namesFile.close()

salesFile = open("sales_data.csv", "w")

for i in sales:
    #The write() method expects a single string argument. If you try to pass a float (or any non-string type), Python will raise a TypeError.
    salesFile.write(str(i) + "\n")
salesFile.close()

# Step 4: Display the sales data in a table format

print("\nSales Report:")
print("Name\t Sales (EUR)")

print("-" * 30)

for i in range(len(salespeople)):  # Single loop
    name = salespeople[i]
    sale = sales[i]
    print(name,"\t", sale)


print("-" * 30)

#Step 5: Display the total sales

totalSales = sum(sales)

print("Total Sales:",totalSales, "EUR")


