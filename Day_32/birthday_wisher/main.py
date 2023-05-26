##################### Extra Hard Starting Project ######################

import smtplib
import random
import datetime as dt
import pandas as pd


# 1. Update the birthdays.csv ✅

my_email = "brandonkwamou@gmail.com"
my_password = "password"

# 2. Check if today matches a birthday in the birthdays.csv ✅

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv ✅


today = dt.datetime.now()


data = pd.read_csv("./birthdays.csv")
birthdays = data.to_dict(orient="records")

for birthday in birthdays:
    if birthday["month"] == today.month and birthday["day"] == today.day:

        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as content:
            letter = content.read().replace("[NAME]", birthday["name"])
            # print(letter)
# letter
# 4. Send the letter generated in step 3 to that person's email address. ✅
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, to_addrs=birthday["email"], msg=f"Subject: Happy Birthday\n\n {letter}")
