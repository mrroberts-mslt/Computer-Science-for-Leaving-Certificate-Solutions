print ("----AVERAGE SPEED CALCULATOR----")

# The original function to calculate average speed
def calculate(d, t):
    speed = d / t
    return speed

'''
Challenge 1: Speed Limit Checker
Create a function that checks if the average speed is breaking a safety limit (e.g., a speed limit of 30 m/s).
Hint: Use an if/else statement inside the function.
'''

def checkSpeedLimit(speed):
    limit = 30  # speed limit in m/s
    if speed > limit:
        print("WARNING: You are speeding! The limit is", limit, "m/s.")
    else:
        print("Safe speed! You are within the limit.")

'''
Challenge 2: Travel Time Estimator
Create a function that uses the calculated avgSpeed to predict how long it would take to travel a much longer distance (like a marathon: 42,195 meters).
Hint: distance divided by speed
'''
def estimateMarathonTime(speed):
    marathonDistance = 42195  # distance in meters
    estimatedTime = marathonDistance / speed
    # Round to 1 decimal place for neatness
    print("At this speed, it would take you", round(estimatedTime, 1), "seconds to finish a marathon.")

'''Challenge 3: Convert to km/h
Average speed in meters per second (m/s) can be hard to visualize for cars. Create a function that converts avgSpeed into kilometers per hour (km/h).
Hint: To convert m/s to km/h, multiply the speed by 3.6.
'''
def convertToKmh(speed):
    speedKmh = speed * 3.6
    print("Your speed in a car would be:", round(speedKmh, 2), "km/h")


# --- Main Program Execution ---

# 1. Get input from the user
distance = int(input("Enter the distance travelled in metres: "))
time = int(input("Enter the time it took to complete the journey in seconds: "))
while time <= 0:
    print("Error time must be greater than 0")
    time = int(input("Please enter a valid time in seconds: "))
# 2. Calculate the average speed
avgSpeed = calculate(distance, time)
print("The average speed is:", round(avgSpeed, 2), "m/s")
print("-----------------------------------")  # Prints a divider line

# 3. Running the challenge functions using avgSpeed
checkSpeedLimit(avgSpeed)
convertToKmh(avgSpeed)
estimateMarathonTime(avgSpeed)
