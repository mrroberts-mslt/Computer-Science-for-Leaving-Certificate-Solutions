def petCalc(pet,food):
    if pet == 1:
        print ((food/1000) * 21 * 3)
    else:
        print ((food/1000) * 21 * 5)

p = int(input("enter pet type 1 = hamster, 2 = cat: "))
f = int(input("enter pet food per day in grams: "))
petCalc(p=pet,f=food)


#Version 2
def hamster():
    return ((food/1000) * 21 * 3)
    
def cat():
    return ((food/1000) * 21 * 5)

def petType():
    if pet == 1:
        print ("your hamster costs €",hamster(),"for 3 weeks")
    else:
        print ("your cat costs €",cat(),"for 3 weeks")
       
pet = int(input("Enter type of Pet 1= Hamster, 2 = Cat :"))
food = int(input("Enter amount of food eaten in grams per day :"))

petType()




