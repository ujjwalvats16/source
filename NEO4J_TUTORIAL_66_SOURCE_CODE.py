
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"))
session=driver.session()

q1='''
MATCH PATH=(A)-[*..1]->(B)
WHERE ALL(x IN NODES(PATH) WHERE x.TEAM="INDIA")
RETURN PATH
'''
result=session.run(q1)
print(list(result))