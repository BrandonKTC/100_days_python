import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"

screen.addshape(img)

turtle.shape(img)
states = pd.read_csv("50_states.csv")
game_is_on = True
guessed_states = []

while game_is_on or len(guessed_states) < 50:
    answer_state = screen.textinput(
        f"Guess the State {len(guessed_states)}/50", "What's another state's name? ").title()

    if answer_state == "Exit":
        game_is_on = False
        break

    if answer_state in states["state"].to_list() and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        df = states[states["state"] == answer_state]
        tim = turtle.Turtle()
        tim.ht()
        tim.penup()
        tim.goto(int(df["x"]), int(df["y"]))
        tim.write(answer_state)
    else:
        print("wrong")

missed_states = [state for state in states["state"].to_list()
                 if state not in guessed_states]

df = pd.DataFrame(missed_states)
df.to_csv("missed_state.csv")


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
