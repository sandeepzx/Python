def disc1(p):
    a = (p * 10) / 100
    return p - a
def disc2(p):
    a = (p*5)/100
    return p - a

n = input("Are You A Student?: (y/n)")
m = input("Are You A Regular Customer?: (y/n)")
amount = int(input("Enter The Amount: "))

if(n=="y" and m == "y"): #if student and regular customer
    y = disc1(disc2((amount)))
    
   
elif(n == "y" and m != "y"):  #only student not regular customer
    y = disc1(amount)
    
   
elif(n != "y" and m == "y"):  #regular customer not a student
    y = disc2(amount)
    
else:                         #no discount
    y = amount   
print(y)