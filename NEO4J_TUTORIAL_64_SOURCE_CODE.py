
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"))
session=driver.session()
q1='''
MATCH (C:EMPLOYEE{NAME:"RAHUL"})<-[R2:FRIENDS]-(A:EMPLOYEE{NAME:"RONI"})
delete R2
'''

session.run(q1)