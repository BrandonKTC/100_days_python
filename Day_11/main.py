from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add_cards(player, times):
    while times > 0:
        player.append(random.choice(cards))
        times -= 1
    return player


def show_cards(player, role):
    if role == "0":
        print(f"Your cards: {player}\nplayer score: {sum(player)}")
    elif role == "1":
        print(
            f"Computer's first card: {player[0]}\ncomputer score: {sum(player)}")
    elif role == "2":
        print(
            f"Computer's final hand: {player}\ncomputer score: {sum(player)}")


def player_lose(player):
    if sum(player) > 21:
        if 11 in player:
            idx = player.index(11)
            player[idx] = 1
            return False
        return True


def check_win(player, dealer):
    if sum(player) > sum(dealer) and sum(player) <= 21:
        print("You Win")
    elif sum(player) == sum(dealer):
        print("It's a Draw")
    else:
        print("You Lost")


play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

while play != 'n':

    player, dealer = [], []
    print("\n"*100)
    print(logo)
    player = add_cards(player, 2)
    dealer = add_cards(dealer, 1)
    # First hand
    show_cards(player, "0")
    show_cards(dealer, "1")

    more = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    # Second hand
    while more != 'n':
        print("\n"*100)
        player = add_cards(player, 1)
        show_cards(player, "0")
        show_cards(dealer, "1")
        if player_lose(player):
            break
        more = input(
            "Type 'y' to get another card, type 'n' to pass: ").lower()

    while sum(dealer) < 17:
        dealer = add_cards(dealer, 1)
    # Final hand
    if not player_lose(player):
        show_cards(player, "0")
        show_cards(dealer, "2")
    check_win(player, dealer)

    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
