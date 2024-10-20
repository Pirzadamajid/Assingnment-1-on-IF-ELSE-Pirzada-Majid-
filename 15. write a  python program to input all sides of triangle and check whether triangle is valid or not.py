a=float(input("enter side a:"))
b=float(input("enter side b:"))
c=float(input("enter side c:"))
if a+b>c and b+c>a and c+a>b:
    print("triangle is valid")
else:
    print("triangle is not valid")