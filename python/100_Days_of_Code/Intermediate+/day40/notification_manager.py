import os
import smtplib
from twilio.rest import Client
from data_manager import DataManager

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")

DUMMY_EMAIL = os.environ.get("DUMMY_EMAIL")
DUMMY_EMAIL_PASSWORD = os.environ.get("DUMMY_EMAIL_PASSWORD")


class NotificationManager:
    def __init__(self):
        # self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        pass

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def _create_email_content(self, flight):
        subject = "New Low Price Flight!"

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += (
                f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            )

        flight_link = f"\nhttps://www.google.com/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        return f"Subject:{subject}\n\n{message+flight_link} "

    def send_emails(self, flight):
        email_content = self._create_email_content(flight)
        data_manager = DataManager()

        user_data = data_manager.get_user_data()

        for user in user_data:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=DUMMY_EMAIL, password=DUMMY_EMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=DUMMY_EMAIL,
                    to_addrs=user["email"],
                    msg=email_content.encode("utf-8"),
                )
