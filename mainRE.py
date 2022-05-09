import requests
import json
r = requests.get("https://reqres.in/api/users")

with open("user.json", "w") as f:
    json.dump(r.json(), f)