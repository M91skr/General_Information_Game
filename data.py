import requests

AMOUNT = 50
parameters = {
    "amount": AMOUNT,
    "type": "boolean",
    "category": 9,
}

question_data = requests.get("https://opentdb.com/api.php", params=parameters)
question_data.raise_for_status()
data = question_data.json()
question_data = data["results"]