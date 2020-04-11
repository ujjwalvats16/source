#tutorial5
#whatsapp bot to get live status update on corona virus
import csv
from pymongo import MongoClient
from flask import Flask ,request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse
import datetime
import urllib
from corona_plot1 import get_data
import os
import io

#region
with io.open("vip.txt","r",encoding="utf-8") as f1:
    data_vip=f1.read()
    f1.close()
    
data_vip=data_vip.split("\n")
print(data_vip)
#database setup
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

@apbot.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()
    num=request.form.get("From")
    print(num)

    # Read a message aloud to the caller
    resp.say("hallo " + num +" ,Thank you for calling! Have a great day.", voice="Polly.Marlene",language="de-DE")

    return str(resp)

@apbot.route("/sms",methods=["get","post"])
def reply():
    num=request.form.get("From")
    num=num.replace("whatsapp:","")
    msg_text=request.form.get("Body")
    print(num)
    x=collection.find_one({"NUMBER":num})
    try:
        status=x["status"] 
    except:
        pass
        
    if(bool(x)==False):   
     collection.insert_one({"NUMBER":num,"status":"first"})
     msg=MessagingResponse()
     resp=msg.message('''Hello , myself teetuu , a bot from total technology:
Utilize my services to get live status update on corona virus.
please select from below ,
*To get country specific data enter country name ,for example if you want to get update for australia please enter australia(not case sensitive)*''')
     return(str(msg))
    else:
        if(status=="first"):
            data=get_data(msg_text,num)
            msg=MessagingResponse()
                #msg1=MessagingResponse()
            resp=msg.message(data)
            #collection.delete_one({"NUMBER":num})
            collection.update_one({"NUMBER":num},{"$set":{"status":"done","last":datetime.datetime.now().timestamp()}})
            
            print(data)
                
            if(data=="*country entered not found*"):
                 print(str(msg))
                 return(str(msg))
             
            else:
                 resp1=msg.message("") 
                 resp1.media("http://5eb275ec.ngrok.io/"+num+".png")
             
                 return(str(msg))  
        if(status=="done"):
            t1=x["last"] 
            t2=datetime.datetime.now().timestamp()
            if(num in data_vip):
                msg=MessagingResponse()
                collection.update_one({"NUMBER":num},{"$set":{"status":"first","last":datetime.datetime.now().timestamp()}})
                resp=msg.message('''Hello , myself teetuu , a bot from total technology:
Utilize my services to get live status update on corona virus.
please select from below ,
*To get country specific data enter country name ,for example if you want to get update for australia please enter australia(not case sensitive)*''')
                return(str(msg))
                
            else:
                if((t2-t1)>1800):
                        msg=MessagingResponse()
                        collection.update_one({"NUMBER":num},{"$set":{"status":"first","last":datetime.datetime.now().timestamp()}})
                        resp=msg.message('''Hello , myself teetuu , a bot from total technology:
Utilize my services to get live status update on corona virus.
please select from below ,
*To get country specific data enter country name ,for example if you want to get update for australia please enter australia(not case sensitive)*''')
                        return(str(msg))
                    
                else:
                        dif=t2-t1
                        dif=(1800-dif)
                        dif=int(dif/60)
                        msg=MessagingResponse()
                        resp=msg.message('''You are not allowed to use the bot at this moment , please try again after'''+
str(dif) + ''' minutes.
If you want to use vip access code please contact roni@totaltechnology.in''') 
                        return(str(msg))  
                          
            
#endregion
if (__name__=="__main__"):
    apbot.run(port=5000)