from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score = 0

        self.score_label = Label(
            text=f"Score: {self.score}", background=THEME_COLOR, fg="#fff")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="#fff")
        self.question = self.canvas.create_text(
            150, 125, width=280, text="Amazon acquired Twitch in August 2014 for $970 million dollars.", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0)
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)
