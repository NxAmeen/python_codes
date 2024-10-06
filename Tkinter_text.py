from tkinter import Tk, Canvas, Label, Entry, Button

# Create the main window
top = Tk()
top.geometry("300x300")

# Create a canvas widget
canvas = Canvas(top, bg="blue", height=250, width=300)
canvas.create_line(10, 10, 200, 200)
canvas.pack()

# Create and place the name label and entry
name_label = Label(top, text="Name")
# name_label.grid(row=0, column=0)

name_entry = Entry(top)
# name_entry.grid(row=0, column=1)

# Create and place the password label and entry
password_label = Label(top, text="Password")
# password_label.grid(row=1, column=0)

password_entry = Entry(top, show="*")
# password_entry.grid(row=1, column=1)

# Create and place the submit button
submit_button = Button(top, text="Submit")
# submit_button.grid(row=2, column=1)

# Run the main event loop
top.mainloop()