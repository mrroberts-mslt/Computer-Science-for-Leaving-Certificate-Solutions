if "a" in ['t', 'y', 'b', 'g']:
    print("It is in the list")
else:
    print ("It is not in the list")
    

myCars = ['Fiat', 'Honda', 'BMW', 'Toyota']
print("Enter a make of car:")
carName = input()
if carName not in myCars:
    print("We do not stock", carName)
else:
    print("Yes, we stock", carName)
