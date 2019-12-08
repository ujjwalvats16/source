from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()

#Constraint creation on name property
q1='''
   create constraint on (a:COMPANY)ASSERT a.name is unique
   '''  
#Constraint validation for name property  
q2='''
    create (a:COMPANY{id:5,name:"google"})
   '''    
   
 
session.run(q2)
    
