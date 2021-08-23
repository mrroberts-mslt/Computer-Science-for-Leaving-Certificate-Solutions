payType = input("Do you want to pay using card, cash or coupon? \n \t:") 
if payType == "cash" :
    print ("Please insert cash.")
elif payType == "card" :
    print("Insert card into the machine.")
else:
    print("Coupons are only accepted at Customer Service.")