notes = (1000,500,200,100,50,20,10,5,1)

amount = int(input("enter amount to be paid $ :"))

for number in notes:
    count = amount//number
    print("note value : ",number,'\tnumber of notes',count)

    amount = amount%number


