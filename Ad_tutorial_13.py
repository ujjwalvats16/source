#tutorial 13
#how to connect ad from a machine which is not domain joined or not in the same network

from ldap3 import Connection,Server
server=Server("62.75.216.81")
con=Connection(server,"totaltechnology\\administrator","Rambo@3322",auto_bind=True)
print(con.extend.standard.who_am_i())
con.search("DC=totaltechnology,DC=com","(objectcategory=person)")
print(con.entries)
