from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()
q2='''
    MERGE(A:PLAYER{NAME:"MESSI"})
ON CREATE SET A.CREATION_TIME=timestamp()
return A.CREATION_TIME
    '''  
q1='''
   MERGE(A:PLAYER{NAME:"MESSI"})
ON CREATE SET A.CREATION_TIME=timestamp(),A.COUNTRY="ARGENTINA"
return A.CREATION_TIME,A.COUNTRY
   '''           
x=session.run(q1)
print(list(x))

