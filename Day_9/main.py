from art import logo

bids = {}
more = True

print(logo)
print("Welcome to the secret auction program.")


def find_highest_bidder(bidding_record):
    bid_name = ""
    max_bid = 0

    for name, bid in bidding_record.items():
        if bid > max_bid:
            max_bid = bid
            bid_name = name

    return bid_name, max_bid


while more:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bids[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if more[0] == 'n':
        more = False
    elif more[0] == 'y':
        print('\n'*100)


max_bidder_name, max_bid = find_highest_bidder(bids)
print('\n'*100)
print(f"The winner is {max_bidder_name} with a bid of ${max_bid}")
