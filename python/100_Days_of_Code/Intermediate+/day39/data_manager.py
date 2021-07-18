import requests

import os

SHEETY_USER_ID = os.environ.get("SHEETY_USER_ID")
SHEETY_URL = f"https://api.sheety.co/{SHEETY_USER_ID}/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_sheet_data(self):
        response = requests.get(url=f"{SHEETY_URL}")
        response.raise_for_status()
        return response.json()["prices"]

    def save_sheet_data(self, sheet_data_row):
        body = {
            "price": sheet_data_row
        }
        response = requests.put(url=f"{SHEETY_URL}/{sheet_data_row['id']}", json=body)
        response.raise_for_status()




