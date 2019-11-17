from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()
q1='''
  MATCH (N)
RETURN N.title AS NAME_PROPERTY
  
   '''  
q2='''
  MATCH (N)
RETURN count(N) AS count_of_nodes 
   '''
q3='''
  MATCH (N)
RETURN count(N) 
   '''  
q4='''
   MATCH (N)
RETURN N.NAME AS NAME_PROPERTY
   '''  
result=session.run(q4)

print(list(result))
