from tkinter import *
from tkinter import messagebox

class sand:
    def __init__(self,root1):
        frame = Frame(root1)
        frame.pack()
        self.L1 = Label(frame,text="Click")
        self.L1.pack()
        self.B1 = Button(frame,text="click here",command= self.click)
        self.B1.pack()
        self.L2 = Label(frame,text="To cancell")
        self.L2.pack()
        self.B2 = Button(frame,text="click here",command= self.mess)
        self.B2.pack()
        self.L3 = Label(frame,text="To quit")
        self.L3.pack()
        self.B3 = Button(frame,text="click here",command= frame.quit)
        self.B3.pack()
    
    def click(self):
        messagebox.showinfo("Message","Clicked")

    def mess(self):
        messagebox.showerror("Error","Cancelled")
    
root = Tk()
obj = sand(root)
root.mainloop()