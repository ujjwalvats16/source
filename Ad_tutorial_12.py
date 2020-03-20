#tutorial 12
#how to set account expiration date in ad user account
from pyad import *
import datetime
from filetimes import dt_to_filetime,utc

user=pyad.adobject.ADObject.from_cn("aalamda")
ed=dt_to_filetime(datetime.datetime(2025,5,11,0,0))

pyad.adobject.ADObject.update_attribute(user,"accountExpires",str(ed))