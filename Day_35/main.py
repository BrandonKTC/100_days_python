import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "cacdd43ad779e6bd48011907a8c327fd"

weather_params = {
    "lat":  48.856614,
    "lon":  2.3522219,
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
    print("bring an umbrella")
