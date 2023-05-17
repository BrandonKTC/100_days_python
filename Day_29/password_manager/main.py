from tkinter import *
from tkinter import messagebox
import json
import random
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = ''.join(random.choice(string.ascii_lowercase +
                                     string.ascii_uppercase + string.digits + string.punctuation) for _ in range(20))
    password_entry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def search_password():
    website = website_entry.get().lower()

    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        try:
            search = data[website]
        except KeyError:
            messagebox.showinfo(title="Website doesn't exist",
                                message="I'm Sorry you havn't register this website yet")
        else:
            email_entry.insert(END, search["email"])
            password_entry.insert(END, search["password"])

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password) != 0:
        with open("data.json", "r") as f:
            data = json.load(f)
            data.update(new_data)
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(column=2, row=1)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
