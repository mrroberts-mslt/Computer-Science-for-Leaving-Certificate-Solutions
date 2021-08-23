carAge = int(input("Enter age of car: "))
carFuel = input("Enter car's fuel type (petrol/diesel): ")
#note boolean needs to be lowercase
if carAge >=10 or carFuel =="diesel":
  print("Pollution level high")
else:
  print("Pollution level low")
