
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"))
session=driver.session()

q2='''
MATCH (A)-[R]->(B)
RETURN STARTNODE(R)
'''



q1='''
MATCH (A)-[R]->(B)
WHERE A.NAME="BOB"
RETURN ENDNODE(R)
'''
result=session.run(q1)
print(list(result))
result=session.run(q2)
print(list(result))