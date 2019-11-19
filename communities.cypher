CALL algo.louvain.stream('disease', 'related', {})
YIELD nodeId, community
MATCH (d:disease) where id(d) = nodeId
RETURN community,
       count(*) as communitySize,
       collect(d.code) as members 
ORDER BY communitySize DESC;