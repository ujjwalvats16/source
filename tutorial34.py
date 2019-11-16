from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()


#without where clause & WITH expression
q1='''
   MATCH (N)
   RETURN (N)

   '''
   
#with where clause & with expression   
q2='''
   MATCH (N)-[R]->(M)
   RETURN TYPE(R)


   
   '''
   
q3='''
   MATCH (N:PERSON)
   RETURN N.NAME



   
   ''' 
q4='''
   MATCH (N)-[R]->(M)
   RETURN *

   '''  
   
q5='''
   WITH ["RONI","MESSI"]AS a
   unwind a as name
   with name
   return name in ["RONI","RAHUL"]


   '''    
         

result=session.run(q5)

print(list(result))
