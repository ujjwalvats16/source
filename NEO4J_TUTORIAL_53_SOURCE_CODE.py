from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session() 
q1='''
MATCH (A:player{NAME:"MESSI"}),(B:Country{NAME:"ARGENTINA"})
MERGE (A)-[C:PLAYED_FOR]-(B)
RETURN A,type(C)
   '''           
x=session.run(q1)
print(list(x))

