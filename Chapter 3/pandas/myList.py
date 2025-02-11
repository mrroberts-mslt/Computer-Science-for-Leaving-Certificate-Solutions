import matplotlib.pyplot as plt
myList=[1,19,27,8,5,9]
plt.plot(myList,"rs")
plt.show()
# for item in myList:
#     if item <0:
#         myList.remove(item)
# print(myList)
myList.sort()
print("Sorted ascending ", myList)
# myList.sort(reverse=True)
# print("Sorted descending ", myList)
# minValue = myList[0]
# maxValue = myList[-1]


minValue = min(myList)
maxValue = max(myList)
print("minimum ", minValue)
print("maximum ", maxValue)

