import os
import requests
from requests.exceptions import HTTPError

SHEETY_USER_ID = os.environ.get("SHEETY_USER_ID","61893ff9233a4273bcf73b1784dfd98b")
SHEETY_URL = f"https://api.sheety.co/{SHEETY_USER_ID}/flightDeals/users"

def run():
    print("Welcome to The Flight Club.")
    print("We find the best flight deals and email them to you.")
    first_name = input("What is your fist name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email?\n")
    email_check = input("Type your email again.\n")
    if email == email_check:
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        try:
            requests.post(url=SHEETY_URL, json=body)
        except HTTPError as e:
            print(f"Error: {e}")
        print("Success! Welcome to the club.")





if __name__ == "__main__":
    run()
