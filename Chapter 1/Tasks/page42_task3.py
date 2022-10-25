
rainfall = 0
rainfallData =[]
weeklyRainfall = 0
for i in range(7):
    rainfall = float(input("Enter rainfall for day: "))
    print("Day",i+1)
    weeklyRainfall += rainfall
    rainfallData.append(rainfall)
print("Weekly Rainfall = ",weeklyRainfall)
avgRainfall = weeklyRainfall / 7
print("Avg Rainfall = ",avgRainfall)
    
for rainamount in rainfallData:
    if rainamount > 3.5:
        print("Yo man its lashing!! on days:",rainamount)
print(rainfallData)

