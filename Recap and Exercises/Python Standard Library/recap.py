import json

with open('data.json') as f:
    loaded = json.load(f)
    print(loaded['name'])