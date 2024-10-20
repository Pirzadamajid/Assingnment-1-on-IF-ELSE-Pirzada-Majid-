week = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
number = int(input("enter week number(between 1-7) : "))
if number < 1 or number > 7:
    print("invalid")
else:
   print("today is ",week[number])
