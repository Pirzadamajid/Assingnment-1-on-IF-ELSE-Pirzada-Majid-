###basic salary<=10000:HRA = 20%,DA = 80%
###basic salary<=20000:HRA = 25%,DA = 90%
###basic salary>20000:HRA = 30%,DA = 95%
###basic = 10000
###if(basic<=10000):
### da=basic * 0.8
###    hra=basic * 0.2
###elif(basic<=20000):
###    da=basic * 0.9
###    hra=basic * 0.25
###else:
###    basic salary >= 20000

###gross=basic + da + hra
###print("The Gross Salary is:-",gross)

basic = int(input("enter the basic salary:-"))
if(basic <= 10000):
    da = basic*0.8
    hra = basic*0.2
elif(basic <= 20000):
    da = basic*0.9
    hra = basic*0.25
else:
    da = basic*0.95
    hra = basic*0.3
gross = basic + da + hra
print("The Gross Salary is :-",gross)





