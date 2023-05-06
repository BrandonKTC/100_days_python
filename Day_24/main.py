# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as t:
    letters = t.read()
    with open("./Input/Names/invited_names.txt") as f:
        for name in f.readlines():
            with open(f'./Output/ReadyToSend/letter_for_{name}.txt', "w") as letter:
                letter.write(letters.replace("[name]", name.strip()))
