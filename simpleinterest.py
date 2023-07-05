p = int(input("Amount:"))
n = int(input("Year:"))
r = float(input("Rate of interest:"))

def interst(p,n,r):
    return (p*n*r)/100

print(interst(p,n,r))