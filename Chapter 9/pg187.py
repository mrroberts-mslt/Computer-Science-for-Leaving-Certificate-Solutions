#below is a nested conditional
#copy the code then change it to use an elif and a boolean operator (or, and, not)
age = int(input("Please enter your age:"))
hasProvisional = input("do you have a provisional licence? (y/n)? ")
#First outer if statement
if age >= 17:
  #inner if statement
  if hasProvisional == "y":
    print("You are eligible to apply for a Driving Licence.")
  else:
    print("You are not eligible to apply for a driving licence. You must get a provisional licence first.")
else:
  print("You are not eligible to apply for a driving licence. You must be 17 first")
