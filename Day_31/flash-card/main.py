from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

data = pd.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def new_word():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(
    FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, pady=50)
# Button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(
    image=wrong_img, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=2)
right_img = PhotoImage(file="./images/right.png")
right_button = Button(
    image=right_img, highlightthickness=0, command=new_word)
right_button.grid(column=1, row=2)

new_word()

window.mainloop()
