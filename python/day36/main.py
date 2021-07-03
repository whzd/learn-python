import os
import requests
import datetime as dt
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_FLUCTUATION_VALUE = 0.5  # %
DATE_YESTERDAY = dt.date.today() - dt.timedelta(1)
DATE_DAY_BEFORE_YESTERDAY = dt.date.today() - dt.timedelta(2)
# API keys
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
SMS_API_KEY = os.environ.get("TWILIO_API_KEY")
# Twilio settings
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_price_change():

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    content = response.json()["Time Series (Daily)"]
    diference = float(content[str(DATE_YESTERDAY)]["4. close"]) - float(
        content[str(DATE_DAY_BEFORE_YESTERDAY)]["4. close"]
    )
    variation = (diference / float(content[str(DATE_YESTERDAY)]["4. close"])) * 100
    return round(variation, 2)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_company_news():

    parameters = {
        "q": COMPANY_NAME,
        "from": DATE_YESTERDAY,
        "sortBy": "popularity",
        "apikey": NEWS_API_KEY,
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    content = response.json()["articles"]
    return f"Headline: {content[0]['title']}\nBrief: {content[0]['description']}\nLink: {content[0]['url']}"


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_sms(stock_fluctuation, news):

    if stock_fluctuation > 0:
        content = f"{STOCK}: ⬆️{abs(stock_fluctuation)}%\n{news}"
    else:
        content = f"{STOCK}: ⬇️{abs(stock_fluctuation)}%\n{news}"

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=content,
        from_="",  # Twilio free trial phone number
        to="",  # Your phone number, that was used in twilio
    )
    print(message.sid)


if __name__ == "__main__":
    stock_fluctuation = get_stock_price_change()
    print(stock_fluctuation)
    if abs(stock_fluctuation) >= STOCK_FLUCTUATION_VALUE:
        news = get_company_news()
        print(news)
        send_sms(stock_fluctuation, news)
