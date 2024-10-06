from tkinter import *
from tkinter import messagebox

top=Tk()
top.geometry("200x200")

def event_handling(event):
    Label(top,text="You clicked the button").pack()

top.bind("<Button-1>",event_handling)

top.mainloop()