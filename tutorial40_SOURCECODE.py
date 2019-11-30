from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()

#OUT DEGREE
q1='''
MATCH (N:PERSON)
WITH [(N)-->(P) WHERE P:PERSON|N.NAME] AS NAMES
UNWIND NAMES AS names
return names , count(names)
   '''  
#IN DEGREE   
q2='''
MATCH (N:PERSON)
WITH [(N)-->(P) WHERE P:PERSON|P.NAME] AS NAMES
UNWIND NAMES AS names
return names , count(names)
   '''    
   
 
result=session.run(q2)

for i in result:
    print(i)
