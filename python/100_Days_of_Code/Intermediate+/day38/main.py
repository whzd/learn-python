import os
import requests
import datetime as dt

# Nutritionix
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.environ.get("NUTRITIONIX_APP_KEY")
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural"

# Sheety
SHEETY_URL = os.environ.get("SHEETY_URL")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


def text_to_data(query):

    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_APP_KEY,
        "Content-Type": "application/json",
    }

    body = {"query": query}

    response = requests.post(
        url=f"{NUTRITIONIX_URL}/exercise", json=body, headers=headers
    )
    response.raise_for_status()
    return response.json()


def save_data_to_sheets(data):
    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    # Date, Time
    date = dt.datetime.now().strftime("%d/%m/%Y")
    time = dt.datetime.now().strftime("%X")
    for exercise in data["exercises"]:
        # Exercise, Duration, Calories
        body = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }
        response = requests.post(url=SHEETY_URL, json=body, headers=headers)
        response.raise_for_status()
        print(response.status_code)


if __name__ == "__main__":
    query = input("Tell me which exercises you did: ")
    print(query)
    data = text_to_data(query)
    print(data)
    save_data_to_sheets(data)
