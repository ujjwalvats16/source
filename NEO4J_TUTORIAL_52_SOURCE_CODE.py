from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session() 
q1='''
merge(A:player{NAME:"CR7"})
ON CREATE SET A.COUNTRY="PORTUGAL"
ON MATCH SET A.POSITION="STRIKER"
RETURN A.NAME,A.COUNTRY,A.POSITION
   '''           
x=session.run(q1)
print(list(x))

