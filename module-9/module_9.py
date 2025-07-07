import requests
response = requests.get("https://pokeapi.co/api/v2/generation/1/")

import json

def jprint(obj):
    text = json.dumps(obj, indent=4)
    print(text)

jprint(response.json())