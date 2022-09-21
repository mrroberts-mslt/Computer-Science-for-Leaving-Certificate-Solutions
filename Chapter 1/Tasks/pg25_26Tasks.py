#solutions page25-26
#Task1
nameArtist = input("Enter your fav artist:")
compliment = " is Brilliant"
print (nameArtist+compliment)

#Task2
myName = input ("Enter your first and last name:")
spaceLoc = myName.index(" ")
print(spaceLoc)
fName= myName[:spaceLoc]
lName= myName[spaceLoc:]
print (fName+lName)

#Task 3
h = int(input("hours:"))
m = int(input("mins:"))
s = int(input("secs:"))
print (h,":",m,":",s)

timeSecs = (h*360)+(m*60)+s
print(timeSecs)

#Task 4
secs = int(input("Enter a 5 digit number for seconds: "))
calc = secs/60
mins = round(calc)
print (mins)

#Task 5 - how can this be convetedto a loop?
key1 = input("Char 1: ")
key2 = input("Char 2: ")
key3 = input("Char 3: ")
key4 = input("Char 4: ")
key5 = input("Char 5: ")

ascii = ord(key1)
print (ascii)

#Task 6
unitsUsed = 684
costPerUnit = 0.19
unitCost = unitsUsed * costPerUnit
standingCharge = 26.20
totalDue = unitCost + standingCharge
print(totalDue)

#convert to input
unitsUsed = int(input("Enter units used per month: "))
costPerUnit = 0.30
unitCost = unitsUsed * costPerUnit
totalDue = unitCost + standingCharge
print(totalDue)
