from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()

q1='''
  match (A{NAME:"VICKY"})-[*2]->(B{NAME:"ROHIT"})

  return A,B
   
   '''
result=session.run(q1)
result=list(result)

if (len(result)>0):
    print("path exists")
    
else:
    print("not exist")    