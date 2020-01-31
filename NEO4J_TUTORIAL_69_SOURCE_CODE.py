
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"))
session=driver.session()

q1='''
MATCH (A)

RETURN PROPERTIES(A)
'''
result=session.run(q1)
print(list(result))