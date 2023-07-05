def final(a,b):
    fp = a / (b**2)
    return fp

x = int(input("Product Price of of X : "))
y = int(input("Product Price of of Y : "))
price = final(x,y)

print("Final Price",price)