def find_maximum(a,b,c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)


n=float(input("enter the first number:"))
m=float(input("enter the second number:"))
o=float(input("enter the third number:"))

print("maximum of three numbers is:",find_maximum(m,n,o))