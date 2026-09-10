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

#task7
fish = 4.50
chips = 2.80
orderFish = int(input("Enter the number of Fish: "))
orderChips = int(input("Enter the number of chips: "))
totalAmt = (orderFish * fish) + (orderChips * chips)
print("The order is for", orderFish,"fish and", orderChips, "chips. The total due is: €",round(totalAmt,2))
vat = 0.09
print("Yo Al you owe the tax man", round(totalAmt*vat,2),"on that last order")

#task8

word = input("Enter a 5 letter word: ")
key = int(input("Enter key (0-25): "))

letter1 = chr((ord(word[0]) - ord('a') + key) % 26 + ord('a'))
letter2 = chr((ord(word[1]) - ord('a') + key) % 26 + ord('a'))
letter3 = chr((ord(word[2]) - ord('a') + key) % 26 + ord('a'))
letter4 = chr((ord(word[3]) - ord('a') + key) % 26 + ord('a'))
letter5 = chr((ord(word[4]) - ord('a') + key) % 26 + ord('a'))

encrypted = letter1 + letter2 + letter3 + letter4 + letter5

print("Encrypted word:", encrypted)
'''
For the example:

Enter a 5 letter word: hello
Enter key (0-25): 5
Encrypted word: mjqqt
The important bit

Take the first letter of hello, which is h:

ord('h')

gives 104.

We subtract ord('a'), which is 97:

104 - 97 = 7

So h is position 7 if a = 0.

Then add the key:

7 + 5 = 12

Position 12 is m.

The % 26 is what makes the alphabet wrap around. For example, y with a key of 3:

y = 24
24 + 3 = 27
27 % 26 = 1
1 = b

So:

y + 3 → b
'''
