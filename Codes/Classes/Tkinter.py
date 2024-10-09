from tkinter import *
top=Tk()
top.geometry("400x400")
top.title("My First GUI")
name=Label(top,text="Name")
name.grid(row=0,column=0)
entry = Entry(top)
entry.grid(row=0,column=1)
password=Label(top,text="Password")
password.grid(row=1,column=0)
entry1 = Entry(top)
entry1.grid(row=1,column=1)

button=Button(top,text="Submit")
button.grid(row=2,column=1)

top.mainloop()