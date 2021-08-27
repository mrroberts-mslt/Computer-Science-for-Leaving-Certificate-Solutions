def volCylinder(radius,height):
  volume = 3.14 *(radius**2) * height
  #The return keyword in Python exits a function and tells Python to run the rest of the main program. A return keyword can send a value back to the main program.
  return volume

#Create the Test data
def unitTest():
  testR = 2
  testH = 1

  expectedVal = 3.14 *(testR**2) * testH
  testAns = volCylinder(testR,testH)

  passed = True
  if expectedVal != testAns:
    passed = False
  return passed
print("Test passed:", unitTest())

def largerNumber(num1,num2):
  if num1 > num2:
    return num1
  else:
    return num2
  
def unitTest():
  firstNums = [1,2,3,4,5]
  secondNums = [1,1,4,-1,100]
  
  fails = 0
  for i in range(len(firstNums)):
    #[i] is the loop position value from the list
    test1 = firstNums[i]
    test2 = secondNums[i]
    testAns = largerNumber(test1,test2)
    if test1 > test2:
      if test1 != testAns:
        fails +=1
     else:
			if test2 != testAns:
				fails +=1
		return fails
	print("Total Fails: ", unitTest())
    
