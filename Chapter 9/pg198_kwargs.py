def piVal():
	return 22 / 7

def volCylinder(height, radius):
    volume = piVal() * (radius ** 2)* height
    print ("The volume is: ", volume)

r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))
#calling the functions below gives 2 different values due to the order
#volCylinder(h,r)
#volCylinder(r,h)

#using a keyword argument to ensure the arguments appear in correct order when calling the function
volCylinder(radius = r, height = h)
