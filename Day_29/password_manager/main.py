from tkinter import *
from tkinter import messagebox
import random
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = ''.join(random.choice(string.ascii_lowercase +
                                     string.ascii_uppercase + string.digits + string.punctuation) for _ in range(20))
    password_entry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(
        title=website, message=f"These are the details entered: \nEmail: {email}"
        f" \nPassword: {password} \n Is it ok to save?")

    if is_ok and password:
        with open("data.txt", "a") as f:
            f.write(f"{website} : email = {email}, password = {password}\n")

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
# Logo
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
