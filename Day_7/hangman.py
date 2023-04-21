import random
from hangman_arts import logo, stages
from hangman_word import word_list

def replace_letter(word_to_guess):
    for idx, letter in enumerate(word):
        if guess == letter:
            word_to_guess[idx] = letter
    return word_to_guess

word = random.choice(word_list)

word_guess = ["_"]*len(word)

guesses = []

lives = 6

print(f"Welcome to :\n {logo}")

while "_" in word_guess and lives > 0:
    print(f"Here is the word: {' '.join(word_guess)}")

    guess = input('guess a letter: ')


    if guess in word and guess not in guesses:
        print("\n"*100)
        guesses.append(guess)
        word_guess = replace_letter(word_guess)
        print(stages[lives])
    elif guess in guesses:
        print("you have already try this letter")
    else:
        guesses.append(guess)
        lives -= 1
        print("\n"*100)
        print(f"{guess} not in the word you lost a live")
        print(stages[lives])

    print(f"guesses: [{','.join(guesses)}]")
    print(' '.join(word_guess))

if '_' not in word_guess:
    print("Yayyy you've Win")
else:
    print("Game Over :'(")