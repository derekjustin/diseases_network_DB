import json

with open("nodes.json",encoding='utf-8-sig', errors='ignore') as f:
     contents = json.load(f, strict=False)

for community in contents:
    print(community['name'])