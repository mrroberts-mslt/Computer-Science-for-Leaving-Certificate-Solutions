petList=[]
totalPets=int(input("How many pets do you have?: "))

if totalPets>0:
    for pet in range(totalPets):
        name=input("Enter pet's name: ")
        petList.append(name)
    print("The names of your pets are: ")
    for pet in range(totalPets):
        print(petList[pet])
else:
    print("Why don't you get a pet?")