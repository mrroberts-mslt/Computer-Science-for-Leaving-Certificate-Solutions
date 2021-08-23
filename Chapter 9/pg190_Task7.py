# see https://realpython.com/python-square-root-function/
import math

a = int(input("enter size of stick A:"))
b = int(input("enter size of stick B:"))
c = int(input("enter size of stick C:"))
if a > b and b > c:
    hypotonuse = a
    opp = c
    adj = b
elif b > a and b > c:
    hypotonuse = b
    opp = a
    adj = c
elif c > a and c > b:
    hypotonuse = c
    opp = b
    adj = a
else:
    hypotonuse = str("All three sides are the same")

triangleSides = opp*opp + adj*adj
calc = math.sqrt(triangleSides)
print(calc)

if calc == hypotonuse:
    print("Yes a right angled triangle is possible")
else:    
    print(math.sqrt(triangleSides),"is not equal to the hypotonuse:", hypotonuse)
    
# solution 2
    
a = int(input("enter size of stick A:"))
b = int(input("enter size of stick B:"))
c = int(input("enter size of stick C:"))

sideA = a*a
sideB = b*b
sideC = c*c
print(sideA, sideB, sideC)

if sideA+sideB == sideC or sideA+sideC == sideB or sideB+sideC == sideA:
  print("Right angled triangle")
else:
  print ("not a right anled triangle")
    
    
