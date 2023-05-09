# import random
# Phonetics = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike",
#              "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "X-Ray", "Yankee", "Zulu"]
# Alphabetics = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
#                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# military = dict(zip(Alphabetics, Phonetics))

import pandas as pd  # 1

alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

military = {row.letter: row.code for (idx, row) in alphabet.iterrows()}

# print(military)
word = input("Enter a word: ").upper()

code = [military[char] for char in word]

print(code)


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# students_scores = {name: random.randint(1, 100) for name in names}

# print(students_scores)

# passed_students = {student: score for (
#     student, score) in students_scores.items() if score >= 60}

# print(passed_students)
