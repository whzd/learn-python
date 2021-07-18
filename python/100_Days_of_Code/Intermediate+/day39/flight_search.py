import os
import requests
from flight_data import FlightData

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_URL = "https://tequila-api.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iataCode(self, city_name):
        header = {"apikey": TEQUILA_API_KEY}

        parameters = {
            "term": city_name,
            "location_types": "airport",
            "limit": 10,
            "active_only": True,
            "sort": "rank",
        }
        response = requests.get(
            url=f"{TEQUILA_URL}/locations/query", params=parameters, headers=header
        )
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def get_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey": TEQUILA_API_KEY}

        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "EUR",
            "max_stopovers": 0,
        }

        response = requests.get(
            url=f"{TEQUILA_URL}/v2/search", params=parameters, headers=header
        )
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: {flight_data.price}€")
        return flight_data
