from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session() 
q1='''
MATCH (a:player{NAME:"MESSI"}),(b:COUNTRY{NAME:"SPAIN"})
MERGE (c:club{NAME:"BARCELONA"})<-[r2:plays_for]-(a)-[r1:lives_in]->(b)
RETURN c.NAME,a.NAME,b.NAME
   '''           
x=session.run(q1)
print(list(x))

