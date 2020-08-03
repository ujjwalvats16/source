from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
import csv
import urllib
import requests
import gridfs

with open("cred.txt")as f1:
    datarow=csv.reader(f1,delimiter=",")
    for row in datarow:
        id=row[0]
        pwd=row[1]
client=MongoClient("mongodb+srv://"+id+":"+urllib.parse.quote(pwd)+"@cluster0-lymvb.mongodb.net/<dbname>?retryWrites=true&w=majority")
db=client["whatsapp_db"]

appbot=Flask(__name__)
@appbot.route("/sms",methods=["GET","POST"])
def reply():
    num=request.form.get("From")
    file_count=int(request.form.get("NumMedia"))
    if(file_count>0):
        msg=MessagingResponse()
        url=request.form.get("MediaUrl0")
        data=requests.get(url,stream=True)
        data.raw.decode_content=True
        fs=gridfs.GridFS(db)
        fs.put(data.raw,filename="tutorial18.png")
        msg_text=msg.message("file has been uploaded")      
    else:
        msg=MessagingResponse()
        msg_text=msg.message("no file received")
        

    return(str(msg))


if __name__=="__main__":
    appbot.run(port=5000)