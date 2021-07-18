import os
import requests

SHEETY_USER_ID = os.environ.get("SHEETY_USER_ID")
SHEETY_URL = f"https://api.sheety.co/{SHEETY_USER_ID}/flightDeals"

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_URL}/prices")
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_URL}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_user_data(self):
        response = requests.get(url=f"{SHEETY_URL}/users")
        data = response.json()
        self.user_data = data["users"]
        return self.user_data

