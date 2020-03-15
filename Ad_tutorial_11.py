#tutorial 11
#get account expiration date from active directory
from pyad import *
from pyad.pyadutils import *
import datetime
user=pyad.aduser.ADUser.from_cn("aalamda")
expirationdate=pyad.pyadutils.convert_datetime(user.get_attribute("accountExpires",False))
print(expirationdate)