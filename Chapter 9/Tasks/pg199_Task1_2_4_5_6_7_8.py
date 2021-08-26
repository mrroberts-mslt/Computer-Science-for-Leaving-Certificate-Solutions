#task1
def happyBday():
  print("Happy Birthday to you")

for i in range(3):
    happyBday()
    
#task2
def piVal():
  print(22/7)
  
piVal()

#task4
#An argument is the value that is sent to the function when it is called.
def myFunction1(baseNum, indexNum):
  print(baseNum ** indexNum)

myFunction1(5, 6) 


#task5
def myFunction2(num1, num2):
  if num1 > num2:
    print(num1, "is larger")
  
  elif num2 > num1:
    print(num2, "is larger")
  
  else:
    print(num1, " and ", num2, "are the same")
    
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
myFunction2(num1, num2) 

#task6
def pondVolume(length,width,depth):
    volume = length * width * depth
    print("Pond volume is: ", volume)
     
length = int(input("enter L: "))
width = int(input("enter W: "))
depth = int(input("enter D: "))
pondVolume(length,width,depth)

#task7
def compareWords(string1, string2):
  if string1 == string2:
    print("Same") 
  else:
    print("Not the same")
    
string1 = input("enter word 1: ")
string2 = input("enter word 2: ")
compareWords(string1, string2)

#task 8 but improved
#checkout https://betterprogramming.pub/how-to-indefinitely-request-user-input-until-valid-in-python-388a7c85aa6e

def checkEmail(email):
    while True:
        try:
            email = input("Enter your email: ")
            if email.__contains__("@") and email.__contains__(".") and len(email) >=8:
                break
            print("Invalid email entered")
        except Exception as e:
            print(e)
email = ()
checkEmail(email)
print("ok lets move on")

