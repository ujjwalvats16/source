from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()
q1=''' 
   create (a:PLAYER{NAME:"MESSI",plays_for:"ARGENTINA"}),(B:PLAYER{NAME:"CR7",plays_for:"PORTUGAL"}),(C:PLAYER{NAME:"POGBA",plays_for:"FRANCE"})
   ''' 
q2='''
    MATCH (A:PLAYER)
MERGE(B:COUNTRY{NAME:A.plays_for})
return A.NAME ,B.NAME
    '''         
x=session.run(q2)
print(list(x))

