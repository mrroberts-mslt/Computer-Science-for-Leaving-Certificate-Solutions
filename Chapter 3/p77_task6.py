#task6 - not finished yet!
salesPerson = ['Bob','Janet','Ellis','Tim','May',]
sales = []
for i in salesPerson:
    file = open("sales.csv", "a")
    sold = input("Enter sales €: ")
    sold = sold + ","
    file.write(sold)  
    file.close()
    file = open("salesperson.csv", "a")
    sP = i + ","
    file.write(sP)
    file.close()
    
    
    
print(sold+sP)
  


file = open("sales.csv", "r")
dataIn = file.read()
file = open("salesperson.csv", "r")
dataP = file.read()


salesList = dataP.split(",")
for i in salesList:
    print(i)

totalList = dataIn.split(",")
totalList.remove(totalList[-1])
totalSales = [float(i) for i in totalList]
total = sum(totalSales)
print(total)

# floatList = []
# for i in totalList:
#     i+=1
#     floatList.append(float(i))
#     i+2
#     print(i)
#    
# 
# print(floatList)



