import matplotlib.pyplot as plt
names =["John","Mary", "Dave","Phillip","Zara","Huw"] 
ages=[12,14,16,17,17,45]
numBS=[2,3,4,1,2,3]
plt.title("Brothers and Sisters")
plt.ylabel("Number")
plt.xlabel("Name")
plt.plot(names, numBS)
plt.plot(ages)
plt.legend(["Num Bros and Sisters", "Age"])
plt.show()