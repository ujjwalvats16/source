from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()


#without where clause & expression
q1='''
   RETURN [x in RANGE(0,10)] 
   AS result 
   '''
   
#without where clause & with expression   
q2='''
   RETURN [x in RANGE(0,10)|x^2] 
   AS result 
   '''   

q3='''
   RETURN [x in RANGE(0,10)WHERE x%2=0|x^2] 
   AS result 
   '''  
#with where clause & with expression   
result=session.run(q3)

print(list(result))
