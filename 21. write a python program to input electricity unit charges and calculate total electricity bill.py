##for first 50 units rs 0.50/unit
##for next 100 units rs 0.75/units
##for next 100 units rs 1.20/units
##for unit above 250 rs 1.50/units
##additional surcharge of 20% is added to the bill

a = int(input("enter units of electricity : "))


if a <=50:
  Base_Amount = a*0.50
  Additional_Surcharge = (Base_Amount*20/100)
  print("BASE AMOUNT: Rs.",Base_Amount)
  print("ADDITIONAL SURCHARGE:Rs.",Additional_Surcharge)
  print("TOTAL ELECTRICITY BILL: Rs.",Base_Amount+Additional_Surcharge)
elif a >50 and a <=150:
    Base_Amount = (25)+(a-50)*0.75
    Additional_Surcharge = (Base_Amount*28/100)
    print("BASE AMOUNT:RS.",Base_Amount)
    print("ADDITIONAL SURCHARGE:Rs.",Additional_Surcharge)
    print("TOTAL ELECTRICITY BILL:Rs.",Base_Amount+Additional_Surcharge)
elif a >150 and a <=250:
    Base_Amount = (100)+(a-150)*1.20
    Additional_Surcharge = (Base_Amount*20/100)
    print("BASE AMOUNT:Rs.",Base_Amount)
    print("ADDITIONAL SURCHARGE:Rs.",Additional_Surcharge)
    print("TOTAL ELECTRICITY BILL:Rs",Base_Amount+Additional_Surcharge)
else:
    Base_Amount = (220)+(a-250)*1.50
    Additional_Surcharge = (Base_Amount*20/100)
    print("TOTAL ELECTRICITY BILL:Rs.",Base_Amount+Additional_Surcharge)
