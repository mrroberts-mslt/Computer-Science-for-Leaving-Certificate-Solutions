# Question 16(b)
# Examination Number:

# This function multiplies two numbers
def multiply(x, y):
  return x * y

# This function divides two numbers
def divide(x, y):
  return x / y

# Main Program
import random # To generate random numbers

print("Select operation.")
print("1.Multiply")
print("2.Divide")
# Take input from the user
choice = input("Enter choice(1/2):")

num1 = random.randint(1,12)
num2 = random.randint(1,12)
if choice == '1':
  print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '2':
  print(num1,"/",num2,"=", divide(num1,num2))
