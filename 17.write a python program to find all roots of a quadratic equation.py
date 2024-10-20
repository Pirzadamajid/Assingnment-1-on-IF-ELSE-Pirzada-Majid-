import cmath


a = int(input("enter number a (a!=o):"))
b = int(input("enter number b:"))
c= int(input("enter number c:"))

d = (b**2) - (4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)
print("\n")
print(f"results for equation,{a}x**2 + {b}x + {c} =0, are :- \n")

if d>0:
    print("two distinct real roots")
elif d==0:
    print("two equal real roots")
elif d<0:
    print("two complex roots")