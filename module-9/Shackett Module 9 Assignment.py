import requests
import json

response = requests.get("http://dnd5eapi.co/api/conditions/blinded")
print(response.status_code)
print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())