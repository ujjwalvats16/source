from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()


#without where clause & WITH expression
q1='''
   MATCH (A:PERSON)
   RETURN [(A)--(B)|B] AS RESULT
   '''
   
#with where clause & with expression   
q2='''
   MATCH (A:PERSON{NAME:"RONALDO"})
   RETURN [(A)--(B)WHERE B:TEAM|B.NAME] AS RESULT

   
   '''   

result=session.run(q2)

print(list(result))
