#whatsapp bot to writeback into database(mongodb)
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import datetime
import csv
import urllib
from pymongo import MongoClient



appbot=Flask(__name__)
@appbot.route("/sms",methods=["GET","POST"])
def reply():
    num=request.form.get("From")
    num=num.replace("whatsapp:","")
    msg_text=request.form.get("Body")
    dt=datetime.datetime.now().strftime("%Y_%m_%d--%H:%M:%S:%p")
    collection.insert({"NUMBER":num,"MESSAGE":msg_text,"TIME":dt})
    msg=MessagingResponse()
    resp=msg.message("your respone has been added to our db")
    return(str(msg))
     
if __name__=="__main__":
    appbot.run()