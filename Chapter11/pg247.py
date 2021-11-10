import csv
#header = ["firstName","lastName","phoneNum","dob","age"]
fName = input("enter fName: ")
lName = input("enter lName: ")
tel = input("enter tel: ")
dob = input("enter dob: ")
age = input("enter age: ")
record1 = [fName,lName,tel,dob,age]

file = open("patients.csv","a", newline ="")
db = csv.writer(file)
#db.writerow(header)
db.writerow(record1)
file.close()
print("Hello")
