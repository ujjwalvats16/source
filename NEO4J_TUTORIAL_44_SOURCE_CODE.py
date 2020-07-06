#tutorial 14
from neo4j import GraphDatabase

driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))

session=driver.session()

q2=''' 
   create (a:COMPANY{name:"google"})
   '''
   
q1=''' 
   drop constraint on (a:COMPANY) ASSERT a.name is unique
   '''   
   
session.run(q2)