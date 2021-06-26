import random
import smtplib
import datetime as dt

SOURCE_EMAIL = "monkeytypemaster@gmail.com"
SOURCE_EMAIL_PASSWORD = "3G70@Pa*V&@dXRzx6IWE"
MONDAY_DOW_VALUE = 5

def get_random_quote_from_file():
    with open("quotes.txt", "r") as f:
        quote_list = f.readlines()
        return random.choice(quote_list)


def send_email(subject, body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=SOURCE_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=SOURCE_EMAIL,
            to_addrs="ilovecsgo_@outlook.com",
            msg=f"Subject:{subject}\n\n{body}"
            )
        connection.close()


if __name__ == "__main__":
    motivational_quote = get_random_quote_from_file()
    if dt.datetime.now().weekday() == MONDAY_DOW_VALUE:
        send_email("Your monday motivational boost is here!", motivational_quote)
