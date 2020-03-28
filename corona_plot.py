#tutorial5
#whatsapp bot to get live status update on corona virus
import csv
from pymongo import MongoClient
from flask import Flask ,request
from twilio.twiml.messaging_response import MessagingResponse
import datetime
import urllib
from corona_plot1 import get_data
import os
#database setup
#region
with open("cred.txt")as f1:
    datarow=csv.reader(f1,delimiter=",")
    for row in datarow:
        id=row[0]
        pwd=row[1]
#endregion
#database connectivity
#region
client=MongoClient("mongodb+srv://"+id+":"+urllib.parse.quote(pwd)+"@cluster0-lymvb.mongodb.net/test?retryWrites=true&w=majority")
db=client["whatsapp_db"]
collection=db["whatsapp_db"]
#endregion#flask part
#region
apbot=Flask(__name__)
@apbot.route("/sms",methods=["get","post"])
def reply():
    num=request.form.get("From")
    num=num.replace("whatsapp:","")
    msg_text=request.form.get("Body")
    x=collection.find_one({"NUMBER":num})
    try:
        status=x["status"]
    except:
        pass
        
    if(bool(x)==False):   
     collection.insert_one({"NUMBER":num,"status":"first"})
     msg=MessagingResponse()
     resp=msg.message("Hello , myself teetuu , a bot from total technology to get live status update on corona virus,please enter country name to get the update ,for example if you want to get update for australia please enter australia(not case sensitive)")
     return(str(msg))
    else:
        if(status=="first"):
            data=get_data(msg_text,num)
            msg=MessagingResponse()
            resp=msg.message(data)
            resp1=msg.message("") 


            collection.delete_one({"NUMBER":num})
            if(data=="country entered not found"):
                return(str(msg))
            else:
             resp1.media("http://48e76b16.ngrok.io/Users/roni/eclipse-workspace/corona_analysis/"+num+".png")
             #os.remove(num+".png")
             return(str(msg))  
            
            


#endregion
if (__name__=="__main__"):
    apbot.run(port=5000)