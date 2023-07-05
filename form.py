from tkinter import *

root = Tk()

L1 = Label(root,text="User Name")
L2 = Label(root,text="Number")
L3 = Label(root,text="Email id")
L4 = Label(root,text="Age")
L5 = Label(root,text="Password")
L6 = Label(root,text="Confirm Password")

N1 = Entry(root)
N2 = Entry(root)
N3 = Entry(root)
N4 = Entry(root)
N5 = Entry(root)
N6 = Entry(root)

B1 = Button(root ,text="login" ,fg="blue" ,bg="white")
B2 = Button(root ,text="cancel" ,fg="blue" ,bg="white")

L1.grid(row=0, column=0)
L2.grid(row=1, column=0)
L3.grid(row=2, column=0)
L4.grid(row=3, column=0)
L5.grid(row=4, column=0)
L6.grid(row=5, column=0)
N1.grid(row=0, column=1)
N2.grid(row=1, column=1)
N3.grid(row=2, column=1)
N4.grid(row=3, column=1)
N5.grid(row=4, column=1)
N6.grid(row=5, column=1)
B1.grid(row=6, column=0)
B2.grid(row=6, column=1)

root.mainloop()