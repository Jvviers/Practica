
LOAD CSV WITH HEADERS FROM 'file:///comment_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:0]->(end);


LOAD CSV WITH HEADERS FROM 'file:///comment_hasCreator_person_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:HASCREATOR]->(end);


LOAD CSV WITH HEADERS FROM 'file:///comment_hasTag_tag_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:HASTAG]->(end);


LOAD CSV WITH HEADERS FROM 'file:///comment_isLocatedIn_place_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:ISLOCATEDIN]->(end);


LOAD CSV WITH HEADERS FROM 'file:///comment_replyOf_comment_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:REPLYOF]->(end);


LOAD CSV WITH HEADERS FROM 'file:///comment_replyOf_post_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:REPLYOF]->(end);


LOAD CSV WITH HEADERS FROM 'file:///forum_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:0]->(end);


LOAD CSV WITH HEADERS FROM 'file:///forum_containerOf_post_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:CONTAINEROF]->(end);


LOAD CSV WITH HEADERS FROM 'file:///forum_hasMember_person_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:HASMEMBER]->(end);


LOAD CSV WITH HEADERS FROM 'file:///forum_hasModerator_person_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:HASMODERATOR]->(end);


LOAD CSV WITH HEADERS FROM 'file:///forum_hasTag_tag_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:HASTAG]->(end);


LOAD CSV WITH HEADERS FROM 'file:///person_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:0]->(end);


LOAD CSV WITH HEADERS FROM 'file:///person_email_emailaddress_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:EMAIL]->(end);


LOAD CSV WITH HEADERS FROM 'file:///person_hasInterest_tag_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:HASINTEREST]->(end);


LOAD CSV WITH HEADERS FROM 'file:///person_isLocatedIn_place_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:ISLOCATEDIN]->(end);


LOAD CSV WITH HEADERS FROM 'file:///person_knows_person_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:KNOWS]->(end);


LOAD CSV WITH HEADERS FROM 'file:///person_likes_comment_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:LIKES]->(end);


LOAD CSV WITH HEADERS FROM 'file:///person_likes_post_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:LIKES]->(end);


LOAD CSV WITH HEADERS FROM 'file:///person_speaks_language_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:SPEAKS]->(end);


LOAD CSV WITH HEADERS FROM 'file:///person_studyAt_organisation_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (or:Organisation {id: row.Organisation.id}), (pl:Place {id: row.Place.id})
MERGE (or)-[:STUDYAT]->(pl);


LOAD CSV WITH HEADERS FROM 'file:///person_workAt_organisation_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (or:Organisation {id: row.Organisation.id}), (pl:Place {id: row.Place.id})
MERGE (or)-[:WORKAT]->(pl);


LOAD CSV WITH HEADERS FROM 'file:///post_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:0]->(end);


LOAD CSV WITH HEADERS FROM 'file:///post_hasCreator_person_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:HASCREATOR]->(end);


LOAD CSV WITH HEADERS FROM 'file:///post_hasTag_tag_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:HASTAG]->(end);


LOAD CSV WITH HEADERS FROM 'file:///post_isLocatedIn_place_0_0.csv' AS row FIELDTERMINATOR '|'
MATCH (start:Node {id: row.StartNode.id}), (end:Node {id: row.EndNode.id})
MERGE (start)-[:ISLOCATEDIN]->(end);

