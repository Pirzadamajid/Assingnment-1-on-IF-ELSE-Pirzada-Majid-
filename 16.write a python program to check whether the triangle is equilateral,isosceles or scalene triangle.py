print ("enter the lengths of the triangle")
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))

if a==b==c:
    print("equilateral")
elif a==b or b==c or c==a:
    print("isosceles")
else:
    print("scalene")