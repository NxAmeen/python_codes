from tkinter import *
from tkinter import messagebox
top=Tk()
def show_message():
    messagebox.showinfo("Message", "Hello World")
button=Button(top,text="Show Message",command=show_message)
button.pack(side=TOP)
top.mainloop()


