import requests
import smtplib
import time
from datetime import datetime

MY_LAT = -51  # Your latitude
MY_LONG = 20  # Your longitude
my_email = "brandonkwamou@gmail.com"
my_password = "password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
while True:

    time.sleep(60)

    if abs(iss_longitude - MY_LONG) < 5 and abs(iss_latitude - MY_LAT) < 5:
        # and it is currently dark
        if time_now.hour >= sunset or time_now.hour <= sunrise:
            # Then send me an email to tell me to look up.
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.ehlo()
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg="Subject: ISS OVERHEAD\n\n Look up")
# BONUS: run the code every 60 seconds.
