from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session() 
q1='''
MATCH (a:person{NAME:"RONI",PHONE:"IPHONE"})
MERGE (a)-[b:has_phone]->(c:phone{NAME:a.PHONE})
RETURN a.NAME,c.NAME
   '''           
x=session.run(q1)
print(list(x))

