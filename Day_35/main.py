import requests

params = {
    "appid": "cacdd43ad779e6bd48011907a8c327fd",
    "lat": "51",
    "lon": "-0.9"
}

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?", params=params)

print(response.json())
