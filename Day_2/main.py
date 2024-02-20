# Challenge 1
# two_digit_number = input("Enter a 2 digit number:\n")
# print(f"{two_digit_number[0]} + {two_digit_number[1]} = {int(two_digit_number[0]) + int(two_digit_number[1])}")

# Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
peoples = int(input("How many people to split the bill? "))
percent = int(input("What percentage tip would you like to give ? 10, 12, or 15? "))
total += (total*percent/100)
print(f"Each person should pay: {round(total/peoples, 2)}")