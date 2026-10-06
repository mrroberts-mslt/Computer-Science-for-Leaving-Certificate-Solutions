#1. Can you work out what is happening here?
print ("----AVERAGE SPEED CALCULATOR----")
#2. Find out what does "def" mean ?
def calculate(d, t):
    speed = d / t
    return speed

# 1. Get input from the user
distance = int(input("Enter the distance travelled in metres: "))
time = int(input("Enter the time it took to complete the journey in seconds: "))

# 2. Calculate the average speed
avgSpeed = calculate(distance, time)
print("The average speed is:", round(avgSpeed, 2), "m/s")
print("-----------------------------------")  # Prints a divider line

'''
Challenge 1: Speed Limit Checker
Create a function that checks if the average speed is breaking a safety limit (e.g., a speed limit of 30 m/s).'''
def checkSpeedLimit(speed):
    limit = 30  # speed limit in m/s
    
'''
Hint: Use an if/else statement inside the function.
Call up the function using: 
'''
checkSpeedLimit(avgSpeed)

'''
Challenge 2: Travel Time Estimator
Create a function that uses the calculated avgSpeed to predict how long it would take to travel a much longer distance (like a marathon: 42,195 meters).
Hint: distance divided by speed
Round to 2 dp
'''

'''Challenge 3: Convert to km/h
Average speed in meters per second (m/s) can be hard to visualize for cars. Create a function that converts avgSpeed into kilometers per hour (km/h).
Hint: To convert m/s to km/h, multiply the speed by 3.6.
Round to 2 dp
'''

