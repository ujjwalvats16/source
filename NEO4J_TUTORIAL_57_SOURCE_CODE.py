from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session() 
q2='''
MATCH (A:PLAYER)
WITH [(A)-[R1:plays]-(B)WHERE B:team|B.NAME] AS TEAMS
RETURN DISTINCT (TEAMS) AS TEAM_NAME
'''
result=session.run(q2)

for i in result:
    print(i)



