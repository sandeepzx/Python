from tkinter import *

root = Tk()

def fun():
    
    print("hi")
Button(root,text="OK", fg="blue" , bg="red", command=fun).pack()
root.mainloop()