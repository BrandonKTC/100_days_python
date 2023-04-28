from art import logo
import random


def game(life):
    live = life
    number = random.randint(1, 100)

    while live:
        print(f"You have {live} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high.")
            live -= 1
        elif guess < number:
            print("Too low.")
            live -= 1
        elif guess == number:
            print(f"You guess it !! The answer was {number}.")
            break
    if not live:
        print("You've run out of gueses, you lose.")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
play = ""

while play not in ['easy', 'hard']:
    play = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if play == 'easy':
        print("\n"*100)
        game(10)
    elif play == "hard":
        print("\n"*100)
        game(5)
    else:
        print("I'm sorry I didn't understand")
