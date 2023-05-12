from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

my_input = Entry(width=10)
my_input.grid(column=1, row=1)
# Label
my_label_miles = Label(text="Miles", font=("Arial", 16))
my_label_miles.grid(column=2, row=1)

my_label = Label(text="is equal to", font=("Arial", 16))
my_label.grid(column=0, row=2)

my_label_con = Label(text="0", font=("Arial", 16))
my_label_con.grid(column=1, row=2)

my_label_km = Label(text="Km", font=("Arial", 16))
my_label_km.grid(column=2, row=2)


def button_clicked():
    my_label_con.config(text=int(my_input.get())*1.6)


# Button
my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=3)

# Entry
# my_input = Entry(width=10)
# my_input.insert(END, "Some text")
# my_input.grid(column=3, row=4)

# my_button_2 = Button(text="New Button")
# my_button_2.grid(column=1, row=3)

# # Text
# textInput = Text(height=5, width=30)
# textInput.focus()
# textInput.insert(END, "Example of multi-line text entry.")
# textInput.pack()
# print(textInput.get("1.0", END))

# Spinbox


# def spinbox_used():
#     print(spinbox.get())


# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# Scale


# def scale_used(val):
#     print(val)


# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# checkButton


# def checkButton_used():
#     print(checked_state.get())


# checked_state = IntVar()
# checkButton = Checkbutton(
#     text="Is On?", variable=checked_state, command=checkButton_used)
# checked_state.get()
# checkButton.pack()

# radioButton


# def radio_used():
#     print(radio_state.get())


# radio_state = IntVar()

# radio_button_1 = Radiobutton(
#     text="Option1", value=1, variable=radio_state, command=radio_used)
# radio_button_2 = Radiobutton(
#     text="Option2", value=2, variable=radio_state, command=radio_used)
# radio_button_1.pack()
# radio_button_2.pack()

# Listbox


# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))


# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]

# for item in fruits:
#     listbox.insert(fruits.index(item), item)
#     listbox.bind("<<ListboxSelect>>", listbox_used)
#     listbox.pack()

window.mainloop()
