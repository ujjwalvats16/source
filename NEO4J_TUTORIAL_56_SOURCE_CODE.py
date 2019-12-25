from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session() 
q2='''
merge (a:player{id:1,email:"test2@gmail.com"})

'''
session.run(q2)



