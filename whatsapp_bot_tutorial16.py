from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
import urllib
import csv

with open("cred.txt")as f1:
    datarow=csv.reader(f1,delimiter=",")
    for row in datarow:
        id=row[0]
        pwd=row[1]
        
client=MongoClient("mongodb+srv://"+id+":"+urllib.parse.quote(pwd)+"@cluster0-lymvb.mongodb.net/<dbname>?retryWrites=true&w=majority")
db=client["whatsapp_db"]
collection=db["users"]
apbot=Flask(__name__)
@apbot.route("/sms", methods=["get","post"])
def reply():
    num=request.form.get("From")
    num=num.replace("whatsapp:","")
    msg=MessagingResponse()
    x=collection.find_one({"NUMBER":num})
    if(x==None):
        resp=msg.message("It seems you are new to our platform ,would you like to register with us, please reply with *yes* or *no*")
    else:
        name=x["NAME"]
        resp=msg.message(f"Welcome back {name},how can we help you today?")
    
   
    
    return(str(msg))

if __name__=="__main__":
    apbot.run(port=5000)