MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cost": 0
}


def make_coffee(coffee, resources):
    for ingredient, quantity in coffee["ingredients"].items():
        resources[ingredient] -= quantity
    resources["cost"] += coffee["cost"]

    return resources


def report():
    for resource, quantity in resources.items():
        if resource in ["water", "milk"]:
            print(f"{resource.title()}: {quantity}ml")
        elif resource == "coffee":
            print(f"{resource.title()}: {quantity}g")
        else:
            print(f"Money: ${quantity}")


def check_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = .25*quarters + .1*dimes + .05*nickles + .01*pennies

    return total


while True:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if choice in ["report", "off"]:
        if choice == "off":
            break
        elif choice == "report":
            report()
    elif choice in ["espresso", "latte", "cappuccino"]:
        if resources["water"] >= MENU[choice]["ingredients"]["water"]:
            coins = check_money()
            resources = make_coffee(MENU[choice], resources)

            if coins >= MENU[choice]["cost"] and resources:
                print(
                    f"Here is ${round(coins - MENU[choice]['cost'],2)} in change.")
                print(f"Here is your {choice} ☕ enjoy")
            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            print("Sorry there is not enough water.")
    else:
        print("I'm sorry I didn't understand")
