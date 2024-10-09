from tkinter import *
from tkinter import messagebox
top=Tk()
agreement=StringVar()

def agreement_state():
    messagebox.showinfo(message=agreement.get())

Checkbutton(top,text='I agree',command=agreement_state,variable=agreement,onvalue='Yes',offvalue='No').pack()

top.mainloop()
