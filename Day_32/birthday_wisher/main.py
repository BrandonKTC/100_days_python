import smtplib

my_email = "brandonkwamou@gmail.com"
my_password = "gkgypsgasccijypk"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.ehlo()
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email,
                    to_addrs="juniorkwamou1@yahoo.com", msg="Hello")
connection.close()
