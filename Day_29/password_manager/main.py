from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
# Logo
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
# Website
# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=4)
# Email/Username
# Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
# Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=4)
# Password:
# Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# Entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=2)
# Button
password_button = Button(text="Generate Password")
password_button.grid(column=3, row=3)
# Add
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=4)

window.mainloop()
