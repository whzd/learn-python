import requests

parameters = {"amount": 10, "type": "boolean"}

result = requests.get(url="https://opentdb.com/api.php", params=parameters)
result.raise_for_status()
question_data = result.json()["results"]
