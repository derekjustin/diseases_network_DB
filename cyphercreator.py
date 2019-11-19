import json
import os

if os.path.exists("labeling.cypher"):
    os.remove("labeling.cypher")

labelcypherfile = open("labeling.cypher", "a")

with open("nodes.json",encoding='utf-8-sig', errors='ignore') as f:
     contents = json.load(f, strict=False)
f.close()

for community in contents:
    if (community["communitySize"] < 10):
        for disease in community["members"]:
            labelcypherfile.write("MATCH( node { code: '" + disease + "'} ) DETACH DELETE node\nWITH 1 as dummy\n")
    else:
        for disease in community["members"]:
            labelcypherfile.write("MATCH( node { code: '" + disease + "'} ) SET node:c" + str(community["community"]) + "\nWITH 1 as dummy\n")

labelcypherfile.close()
