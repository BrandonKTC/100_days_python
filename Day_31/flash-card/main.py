from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=flash_card)
# Label
canvas.create_text(400, 150, text="French", font=(FONT, 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2, pady=50)


# Button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=2)
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=2)


window.mainloop()
