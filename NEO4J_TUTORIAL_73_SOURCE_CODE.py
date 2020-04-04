
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"),encrypted=False)
session=driver.session()
q1='''
create (a:EMPLOYEE{NAME:"RAHUL"})
create (b:EMPLOYEE{NAME:"VICKY"})
'''
q2='''
MATCH (a:EMPLOYEE{NAME:"RAHUL"})
MATCH (b:EMPLOYEE{NAME:"VICKY"})
CREATE (a)-[:knows{for_years:10}]->(b)
'''
session.run(q1)
session.run(q2)
