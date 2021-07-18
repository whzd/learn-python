import requests
import datetime as dt

from requests.models import Response

USERNAME = "whzd"
TOKEN = "verysecretcodeomg"
PIXELA_URL = "https://pixe.la/v1/users/"
GRAPH_ID = "graph1"

# Create a user
user_parameters = {
    "token": "verysecretcodeomg",
    "username": "whzd",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_URL, json=user_parameters)
# print(response.text)

# Create a graph
graph_parameters = {
    "id": "graph1",
    "name": "Meditation Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=f"{PIXELA_URL}whzd/graphs", json=graph_parameters, headers=headers)
# print(response.text)

# Create a pixel
pixel_parameters = {
    # "date": str(dt.date.today()).replace("-", ""),
    "date": dt.datetime.now().strftime("%Y%m%d"),
    "quantity": "5"
}

# response = requests.post(url=f"{PIXELA_URL}{USERNAME}/graphs/{GRAPH_ID}", json=pixel_parameters, headers=headers)
# response.raise_for_status()
# print(response.json())

date = dt.datetime.now().strftime("%Y%m%d")

# Update a pixel
# response = requests.put(url=f"{PIXELA_URL}{USERNAME}/graphs/{GRAPH_ID}/{date}", json={"quantity": "10"}, headers=headers)
# print(response.json())

# Delete a pixel
response = requests.delete(url=f"{PIXELA_URL}{USERNAME}/graphs/{GRAPH_ID}/{date}", headers=headers)
print(response.json())
