import tkinter

window = tkinter.Tk()

window.title("My GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="My Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


def button_clicked():
    my_button.config(command=my_input.get())


# Button
my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.grid(column=2, row=2)

# Entry
my_input = tkinter.Entry(width=10)
my_input.insert(tkinter.END, "Some text")
my_input.grid(column=3, row=4)

my_button_2 = tkinter.Button(text="New Button")
my_button_2.grid(column=1, row=3)

# # Text
# textInput = tkinter.Text(height=5, width=30)
# textInput.focus()
# textInput.insert(tkinter.END, "Example of multi-line text entry.")
# textInput.pack()
# print(textInput.get("1.0", tkinter.END))

# Spinbox


# def spinbox_used():
#     print(spinbox.get())


# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# Scale


# def scale_used(val):
#     print(val)


# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# checkButton


# def checkButton_used():
#     print(checked_state.get())


# checked_state = tkinter.IntVar()
# checkButton = tkinter.Checkbutton(
#     text="Is On?", variable=checked_state, command=checkButton_used)
# checked_state.get()
# checkButton.pack()

# radioButton


# def radio_used():
#     print(radio_state.get())


# radio_state = tkinter.IntVar()

# radio_button_1 = tkinter.Radiobutton(
#     text="Option1", value=1, variable=radio_state, command=radio_used)
# radio_button_2 = tkinter.Radiobutton(
#     text="Option2", value=2, variable=radio_state, command=radio_used)
# radio_button_1.pack()
# radio_button_2.pack()

# Listbox


# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))


# listbox = tkinter.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]

# for item in fruits:
#     listbox.insert(fruits.index(item), item)
#     listbox.bind("<<ListboxSelect>>", listbox_used)
#     listbox.pack()

window.mainloop()
