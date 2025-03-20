import random

def thermostatModel(actual, target):
    if actual < target:
        return 1  # Heater ON
    else:
        return 0  # Heater OFF

targetTemp = int(input("Enter target temp: "))  # Target temperature
for i in range(100):  # Loop 100 times
    actualTemp = random.randint(10, 30)  # Random temperature between 10 and 30
    tempOnorOff = thermostatModel(actualTemp, targetTemp)
    print("Actual: " + str(actualTemp) + ", Target: " + str(targetTemp) + ", Heater: " + str(tempOnorOff))

