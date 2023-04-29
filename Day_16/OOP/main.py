from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:

    choice = input(f"What would you like? ({Menu.get_items()})").lower()

    if choice in ["report", "off"]:
        if choice == "off":
            break
        elif choice == "report":
            coffee_maker.report()
    elif choice in ["latte", "espresso", "cappuccino"]:
        if coffee_maker.is_resource_sufficient(Menu.find_drink(choice)):
            if money_machine.make_payment(Menu.find_drink(choice).cost):
                coffee_maker.make_coffee(Menu.find_drink(choice))
            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            print("Sorry there is not enough water.")
    else:
        print("I'm sorry I didn't understand")
