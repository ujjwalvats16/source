
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"))
session=driver.session()

q1='''
MATCH (A)
SET A:india:banglore
'''
session.run(q1)