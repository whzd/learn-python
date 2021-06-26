import random
import pandas
import smtplib
import datetime as dt

SOURCE_EMAIL = "monkeytypemaster@gmail.com"
SOURCE_EMAIL_PASSWORD = "3G70@Pa*V&@dXRzx6IWE"


# Check if today matches a birthday in the birthdays.csv
def _import_birthdays_file():
    return pandas.read_csv("./birthdays.csv").to_dict(orient="records")


def check_if_birthday():
    entries = _import_birthdays_file()
    for entry in entries:
        if dt.date(year=entry["year"], month=entry["month"], day=entry["day"]) == dt.date.today():
            send_birthday_email(entry["name"], entry["email"])


# Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def _get_email_content(name):
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as f:
        return f.read().replace("[NAME]", name)


# Send the letter generated to that person's email address.
def send_birthday_email(name, email):
    subject = "Hip Hip Hooray!"
    body = _get_email_content(name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=SOURCE_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=SOURCE_EMAIL,
            to_addrs=email,
            msg=f"Subject:{subject}\n\n{body}"
            )
        connection.close()

if __name__ == "__main__":
    check_if_birthday()
