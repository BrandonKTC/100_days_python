import datetime as dt
import smtplib
import random

my_email = "brandonkwamou@gmail.com"
my_password = "password"

now = dt.datetime.now()
day_week = now.weekday()
if day_week == 0:
    quotes = open('./quotes.txt').read().splitlines()
    quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:'motivational daily quotes'\n\n{quote}.")
