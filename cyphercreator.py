import json

with open('formattednodes.json', 'r') as f:
    contents = json.load(f)

for community in contents:
    print(community['members'])