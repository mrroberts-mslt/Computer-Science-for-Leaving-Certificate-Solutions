#Task1
age = int(input("Please enter your age:"))
score = int(input("Enter your score: "))
#First outer if statement
if age <= 16 and score >= 80 :
  print("Excellent")
elif age > 16 and score >= 80 :
  print("Good")
else:
  print("Try harder")
