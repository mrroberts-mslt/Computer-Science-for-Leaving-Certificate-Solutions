hours = [12,7,9,9,6,8,2]
vol = 0.5
cost = 1.35
total = 0
for i in range(len(hours)): 
    total = total + hours[i] 

print("Stephen you have stayed here for this number of hours: ",total)
litresDrank = total*vol
print("You greedy boy you drank: ",litresDrank,"litres!")
calc = cost*litresDrank
print("you owe me this much money! €",round(calc,2))
