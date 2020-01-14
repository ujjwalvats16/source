
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"))
session=driver.session()
q1="""
match (n:JEANS)
with (n) limit 2
delete (n)
"""
q2="""
match (n:JEANS)
return count(n)
"""
session.run(q1)
result=session.run(q2)
print(list(result))
    
    


