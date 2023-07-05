def div(a,b):
    try: 
        c = a / b
        return c
    except:
        print("Division by Zero Error, Please don't insert zero")
    finally:
        print("Done")
x = int(input("Enter the Divident:"))
y = int(input("Enter the Divisor:"))
print(div(x,y))