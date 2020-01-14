
from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri=("bolt://localhost:7687"),auth=("neo4j","Rambo@1234"))
session=driver.session()
qs="""
match (n:SHIRTS)
with (n) limit 1
delete (n)
"""
qsd="""
match (n:SHIRTS)
return count(n)
"""
qt="""
match (n:TSHIRTS)
with (n) limit 1
delete (n)
"""
qtd="""
match (n:TSHIRTS)
return count(n)
"""
qj="""
match (n:JEANS)
with (n) limit 1
delete (n)
"""
qjd="""
match (n:JEANS)
return count(n)
"""
print("enter your choice , enter 1 for shirts,2 for tshirts,3 for jeans")
s=input("enter your choice")
s=int(s)
if(s==1):
 session.run(qs)
 result=session.run(qsd)
 print(list(result))
if(s==2):
 session.run(qt)
 result=session.run(qtd)
 print(list(result))
if(s==3):
 session.run(qj)
 result=session.run(qjd)
 print(list(result))   
    
    


