from art import logo


def add(n1, n2):
    return n1 + n2


def soustract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": soustract,
    '/': divide,
    '*': multiply
}


def calculator():
    num1 = float(input("What's the first number?: "))

    while True:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the lines above: ")

        first = True
        num2 = float(input("What's the second number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(
            f"{num1} {operation_symbol} {num2} = {round(answer,2)}")

        again = input(
            f"Type 'y' to continue calculating with {round(answer,2)}, or type 'n' to exit.: ").lower()

        if again == 'n':
            break
        elif again == 'y':
            num1 = answer


print(logo)
calculator()
