import random

choices = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", 
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

gameOn = input("Do you want to play Rock | Paper | Scissors ? Y or N:\n").lower()

while gameOn == "y":

    user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice = random.randint(0,2)
    if user_choice in range(3):
        print(choices[user_choice])
        print("Computer chose:")
        print(choices[computer_choice])

        if user_choice == 0:
            if computer_choice == 0:
                print("It's a draw!")
            elif computer_choice == 1:
                print("You lose 💀")
            elif computer_choice == 2:
                print("You WIN!")
        elif user_choice == 1:
            if computer_choice == 0:
                print("You WIN!")
            elif computer_choice == 1:
                print("It's a draw!")
            elif computer_choice == 2:
                print("You lose 💀")
        elif user_choice == 2:
            if computer_choice == 0:
                print("You lose 💀")
            elif computer_choice == 1:
                print("You WIN!")
            elif computer_choice == 2:
                print("It's a draw!")
    else:
        print("Wrong choice please Try again!\n")
        
    gameOn = input("Do you want to play Rock | Paper | Scissors ? Y or N:\n").lower()

print('Thank you for playing 🤪')