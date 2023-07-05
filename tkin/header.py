from tkinter import *

root = Tk()
toolbar = Frame(root,bg="pink")

send = Button(toolbar,text="send",command=root.quit)
send.pack(side=LEFT,padx=20,pady=20)
toolbar.pack(side=TOP,fill=X)
footer = Label(root,text="this is a footer",bd=20,relief="sunken",anchor=W)
footer.pack(side=BOTTOM,fill=X)

root.mainloop()