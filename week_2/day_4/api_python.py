import requests 
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

response = requests.get("https://api.chucknorris.io/jokes/random")

print(response)

data = response.json()
print(data)
print(data["value"])
print(data.get("value")) #avoid breaking the code

with open(dir_path + '/jokes.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False) 
    print("file was created")

