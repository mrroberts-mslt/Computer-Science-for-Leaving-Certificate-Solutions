iCost= float(input("Enter the initial cost of the item in euro: "))
vatRate = float(input("Enter the VAT rate as a percentage: "))
finalCost = iCost * (100+vatRate)/100
totalVat = finalCost - iCost
totalVat = round(totalVat, 2)
finalCost = round(finalCost,2)
print ("The final cost in euro after VAT is", finalCost)
print ("The total VAT amount in euro is", totalVat)

