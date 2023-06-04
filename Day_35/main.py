import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "cacdd43ad779e6bd48011907a8c327fd"
account_sid = "AC99482de55ddc023fe19665ccdb5e4e49"
auth_token = "b64e37af264e187cdb7f292a86d27581"

weather_params = {
    "lat":  43.769562,
    "lon":  11.255814,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(
    OWM_Endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+13203788034",
        to="YOUR PHONE NUMBER"
    )
