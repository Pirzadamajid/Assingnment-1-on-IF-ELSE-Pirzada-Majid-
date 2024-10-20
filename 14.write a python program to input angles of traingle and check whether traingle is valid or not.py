a = int(input("enter first angle:"))
b = int(input("enter second angle:"))
c= int(input("enter third angle:"))

if a + b + c == 180 and a!=0 and b!=0 and c!=0:
    print("possible")
else:
    print("not possible")