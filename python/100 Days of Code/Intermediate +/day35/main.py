import os
import requests
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

parameters = {
    "lat": 46.947975, # Your location latitude
    "lon": 7.447447,  # Your location longitude
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters
)
response.raise_for_status()
ofh_weather_data = response.json()["hourly"][:12]

will_rain = False

for weather in ofh_weather_data:
    if 232 < weather["weather"][0]["id"] < 700 and not will_rain:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="It's going to rain today.\nDon't forget the umbrella.",
        from_="", # Twilio free trial phone number
        to="",   # Your phone number, that was used in twilio
    )
    print(message.status)
