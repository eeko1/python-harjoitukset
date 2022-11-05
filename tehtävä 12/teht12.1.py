import requests

chuck_joke = "https://api.chucknorris.io/jokes/random"

response = requests.get(chuck_joke).json()

print(response["value"])

