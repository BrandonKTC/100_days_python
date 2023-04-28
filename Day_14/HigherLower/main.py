from art import logo, vs
from game_data import data
import random

score = 0


def print_attr(person, first=False):
    if first:
        print(
            f"Compare A: {person['name']}, a {person['description']} from {person['country']}.")
    else:
        print(
            f"Against B: {person['name']}, a {person['description']} from {person['country']}.")


while True:

    first_person = random.choice(data)
    second_person = random.choice(data)
    print("\n"*100)
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print_attr(first_person, True)
    print(vs)
    print_attr(second_person)

    answer = ""
    while answer not in ["A", "B"]:
        answer = input("\nWho has more followers? Type 'A' or 'B' ").upper()

    if answer == 'A' and first_person["follower_count"] > second_person["follower_count"] or answer == 'B' and first_person["follower_count"] < second_person["follower_count"]:
        score += 1
    else:
        print("\n"*100)
        print(logo)
        print(f"\nSorry that's wrong. Final score: {score}")
        break
