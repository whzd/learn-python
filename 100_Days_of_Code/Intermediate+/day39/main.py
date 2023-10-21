# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
import datetime as dt

def run():
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    data = data_manager.get_sheet_data()

    origin_code = "" # Your closest airport iataCode
    tomorrow = dt.datetime.now() + dt.timedelta(days=1)
    six_months_ahead = dt.datetime.now() + dt.timedelta(days=6 * 30)

    for city in data:
        if city["iataCode"] == "":
            city["iataCode"] = flight_search.get_iataCode(city["city"])
            data_manager.save_sheet_data(city)
        else:
            flight = flight_search.get_flight(origin_city_code=origin_code, destination_city_code=city["iataCode"], from_time=tomorrow, to_time=six_months_ahead)

            if flight:
                if flight.price < city["lowestPrice"]:
                    notification_manager.send_sms(
                        message=f"Low price alert! Only {flight.price}€ to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
                    )


if __name__ == "__main__":
    run()
