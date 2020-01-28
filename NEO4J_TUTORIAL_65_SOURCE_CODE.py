
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"))
session=driver.session()
q1='''
match PATH=(A:EMPLOYEE)-[*1..2]->(B:EMPLOYEE)
WHERE A.NAME="RONI" AND B.NAME="MARK"
RETURN NODES(PATH)
'''

result=session.run(q1)
print(list(result))