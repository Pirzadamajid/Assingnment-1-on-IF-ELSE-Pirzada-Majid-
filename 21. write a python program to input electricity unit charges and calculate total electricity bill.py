##for first 50 units rs 0.50/unit
##for next 100 units rs 0.75/units
##for next 100 units rs 1.20/units
##for unit above 250 rs 1.50/units
##additional surcharge of 20% is added to the bill

unit = int(input("enter unit :"))
if unit <= 50:
    bill = unit * 0.50
elif unit >= 50  <= 150:
    bill = unit * 0.75
elif unit >= 150 <= 250:
    bill = unit * 1.20
elif unit > 250:
    bill = unit * 1.50
else:
    bill = unit * 20

print("Total Bill :",bill)
