### 90>= 'A'
###80>= 'B'
### 70>= 'C'
### 60>= 'D'
### 40>= 'E'
### 40<= 'reappear'


e = int (input("enter marks for english :"))
u = int (input("enter marks for urdu :"))
m = int (input("enter marks for maths :"))
sst = int (input("enter marks for sst :"))
s = int (input("enter marks for science :"))

tot= e+u+m+sst+s
per=tot/5

if per>=90 :
     grade='A'
elif per>=80 :
     grade='B'
elif per>=70 :
     grade='C'
elif per>=60 :
     grade='D'
elif per>=40 :
     grade='E'
else:
    grade='reappear'

print("Total marks:",tot)
print("percentage : ",per)
print("Grade :",grade)