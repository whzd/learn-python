import time
import smtplib
import requests
from datetime import datetime


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
MY_EMAIL = "" # Your email
MY_EMAIL_PASSWORD = "" # Your password


def _is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude)
    print(iss_longitude)

    #Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5


def _is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    current_hour = datetime.now().hour()
    print(current_hour)

    return current_hour < sunrise or current_hour > sunset


def _send_email(subject, body):
    with smtplib.SMTP("smtp.gmail.com") as connection:      # the smtp server of your email provider
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:{subject}\n\n{body}"
            )

def run():
    # Check every 60 seconds
    while True:
        if _is_iss_overhead() and _is_night_time():
                _send_email("ISS is overhead right now!", "Look at the sky!")
        time.sleep(60)


if __name__ == "__main__":
    run()
