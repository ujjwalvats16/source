from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()



q1='''
   MATCH (N:PERSON{NAME:"RONALDO"})
  UNWIND [(N)-->(P) WHERE P:TEAM|P.NAME] AS TEAMS
  WITH TEAMS
   where TEAMS IN ["BRAZIL","ARGENTINA","FRANCE","PORTUGAL"]
   return TEAMS



   
   '''
    
q2='''
   MATCH (N:PERSON{NAME:"RONALDO"})
  UNWIND [(N)-->(P) WHERE P:TEAM|P.NAME] AS TEAMS
  WITH TEAMS
   TEAMS IN ["BRAZIL","ARGENTINA","FRANCE","PORTUGAL"]



   
   '''
           

result=session.run(q1)

print(list(result))
