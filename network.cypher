call apoc.load.json("file:///network.json")
YIELD value as node
MERGE (a:disease {code: node.a.id, name: node.a.name})
MERGE (b:disease {code: node.b.id, name: node.b.name})
CREATE (a)-[r:related {weight: node.weight}]->(b);
