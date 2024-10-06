# from tkinter import *
# top=Tk()
# menubar=Menu(top)
# menubar.add_command(label="File")
# menubar.add_command(label="View")
# top.config(menu=menubar)
# top.mainloop()

from tkinter import *

top = Tk()
def file_command():
    print("File command")

menubar = Menu(top)

file_menu = Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=file_command)
file_menu.add_command(label="Open")

top.config(menu=menubar)
top.mainloop()