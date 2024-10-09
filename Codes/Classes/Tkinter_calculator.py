# from tkinter import *
# from tkinter import messagebox

# top=Tk()
# top.geometry("800x800")

# radio=IntVar()

# def perform_operations():

#     n1=int(e.get())
#     n2=int(e1.get())

#     if radio.get()==0:
#         messagebox.showwarning("Error","Please select an operation")
#         return

#     if radio.get()==1:
#         result=add(n1,n2)
#     elif radio.get()==2:
#         result=subtract(n1,n2)
#     elif radio.get()==3:
#         result=multiply(n1,n2)
#     elif radio.get()==4:
#         result=divide(n1,n2)
#     else:
#         print("Invalid Operation")

#     result_text.delete(1,END)
#     result_text.insert(END,f'Result:{result}')

# def add(n1,n2):
#     return n1+n2
# def subtract(n1,n2):
#     return n1-n2
# def multiply(n1,n2):
#     return n1*n2
# def divide(n1,n2):
#     return n1/n2

# first_number=Label(top,text="First Number")
# first_number.grid(row=0,column=0)
# e=Entry(top)
# e.grid(row=0,column=1)

# second_number=Label(top,text="Second Number")
# second_number.grid(row=1,column=0)
# e1=Entry(top)
# e1.grid(row=1,column=1)

# r=Radiobutton(top,text="Add",variable=radio,value=1)
# r.grid(row=2,column=0)
# r1=Radiobutton(top,text="Subtract",variable=radio,value=2)
# r1.grid(row=2,column=1)
# r2=Radiobutton(top,text="Multiply",variable=radio,value=3)
# r2.grid(row=2,column=2)
# r3=Radiobutton(top,text="Divide",variable=radio,value=4)
# r3.grid(row=2,column=3)

# button=Button(top,text="Calculate",command=perform_operations)
# button.grid(row=4,column=3)

# result_text=Text(top,height=2,width=20)
# result_text.grid(row=5,column=1)

# top.mainloop()



from tkinter import *
from tkinter import messagebox

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def perform_operations():
    n1 = float(e.get())
    n2 = float(e1.get())
    operation = radio.get()
    if operation == 0:
        messagebox.showwarning("Error", "Please select an operation")
        return
    if operation == 1:
        result = add(n1, n2)
    elif operation == 2:
        result = subtract(n1, n2)
    elif operation == 3:
        result = multiply(n1, n2)
    elif operation == 4:
        result = divide(n1, n2)
    result_text.delete(1.0, END)
    result_text.insert(END, str(result))

top = Tk()

first_number = Label(top, text="First Number")
first_number.grid(row=0, column=0)
e = Entry(top)
e.grid(row=0, column=1)

second_number = Label(top, text="Second Number")
second_number.grid(row=1, column=0)
e1 = Entry(top)
e1.grid(row=1, column=1)

radio = IntVar()
r = Radiobutton(top, text="Add", variable=radio, value=1)
r.grid(row=2, column=0)
r1 = Radiobutton(top, text="Subtract", variable=radio, value=2)
r1.grid(row=2, column=1)
r2 = Radiobutton(top, text="Multiply", variable=radio, value=3)
r2.grid(row=2, column=2)
r3 = Radiobutton(top, text="Divide", variable=radio, value=4)
r3.grid(row=2, column=3)

button = Button(top, text="Calculate", command=perform_operations)
button.grid(row=4, column=3)

result_text = Text(top, height=2, width=20)
result_text.grid(row=5, column=1)

top.mainloop()