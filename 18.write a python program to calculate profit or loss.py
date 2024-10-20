sp = float(input("enter selling price:-"))
cp = float(input("enter cost price:-"))
if(sp>cp):
    amount= sp-cp
    print("profit")
elif(cp>sp):
    amount= cp-sp
    print("loss")
else:
    print("no loss no profit")