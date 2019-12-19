from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session() 
q1='''
 MERGE (A:PLAYER{NAME:"POGBA"})
ON MATCH SET A.COUNTRY="FRANCE"
RETURN A.NAME,A.COUNTRY
   '''           
x=session.run(q1)
print(list(x))

