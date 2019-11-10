from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()


q1='''
   match (a)<--(b)-->(c)
   return a,b,c
   
   '''

result=session.run(q1)

for i in result:
    print(i)