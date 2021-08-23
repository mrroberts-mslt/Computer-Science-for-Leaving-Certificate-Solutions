print("1 Calculate the area or a circle")
print("2 Calculate the volume of a sphere")
print("3 Exit")

option = int(input("Enter option (1-3): "))
while (option !=3):
    if option == 1:
        r= float(input("Enter the radius: "))
        area = 3.14*(r**2)
        print("Area is: ", area)
        option = 0
    elif (option ==2):
        r = float(input("Enter the radius: "))
        vol = (4/3)*(3.14*(r**3))
        print ("Volume is: ", vol)
        option = 0
    else:
        print("Invalid choice")
    print("1 Calculate the area or a circle")
    print("2 Calculate the volume of a sphere")
    print("3 Exit")
    option = int(input("Enter option (1-3): "))
print("Time for a rest")        
        
