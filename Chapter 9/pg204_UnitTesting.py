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
