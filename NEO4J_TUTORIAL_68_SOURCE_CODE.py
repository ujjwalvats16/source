
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"))
session=driver.session()

q1='''
MATCH (N)
REMOVE N:EMPLOYEE:TEAMLEAD:TESTING
'''
session.run(q1)