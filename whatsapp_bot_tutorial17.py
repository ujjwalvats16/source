from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
import urllib
import csv
import random
from datetime import datetime
import smtplib, ssl
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open("cred.txt")as f1:
    datarow=csv.reader(f1,delimiter=",")
    for row in datarow:
        id=row[0]
        pwd=row[1]


def send_mail(mail,otp):
    sender_email = "ronidas071@gmail.com"
    receiver_email = mail
    password = pwd
    message = MIMEMultipart("alternative")
    message["Subject"] = "otp from Total Technology"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = f"""\
    Hi,
    How are you?
    please use the otp:{otp} for verification"""
    
    body = MIMEText(text, "plain")
    
    message.attach(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
             
client=MongoClient("mongodb+srv://"+id+":"+urllib.parse.quote(pwd)+"@cluster0-lymvb.mongodb.net/<dbname>?retryWrites=true&w=majority")
db=client["whatsapp_db"]
collection=db["users"]
apbot=Flask(__name__)
@apbot.route("/sms", methods=["get","post"])
def reply():
    num=request.form.get("From")
    msg_text=request.form.get("Body").lower()
    num=num.replace("whatsapp:","")
    msg=MessagingResponse()
    x=collection.find_one({"NUMBER":num})
    if(x==None):
        collection.insert_one({"NUMBER":num,"status":"new"})
        resp=msg.message("It seems you are new to our platform ,would you like to register with us, please reply with *yes* or *no*")
    else:
        if(x["status"]=="new"):
            if(msg_text=="yes"):
                collection.update_one({"NUMBER":num},{"$set":{"status":"input","last":datetime.now().timestamp()}})
                resp=msg.message("""*Please enter your name & emailaddress separated by comma*\n,*for example if your nam is john and email address is john@example.com ,then you should write john,john@example.com*""")
            elif(msg_text=="no"):
                resp=msg.message("""*thank you very much ,but you cant proceed without register*""")
                
            else:
                resp=msg.message("""*invalid input please enter yes or no*""")
                
               
        if(x["status"]=="input"):
            try:
             user_input=msg_text.split(",")
             otp=random.randint(1000,9999)
             mail=user_input[1]
             send_mail(mail, otp)
             resp=msg.message(f"we have sent otp to your registered email id {mail}")
             collection.update_one({"NUMBER":num},{"$set":{"NAME":user_input[0],"otp":otp,"EMAIL":user_input[1],"status":"added","last":datetime.now().timestamp()}})
             
            except Exception as e:
                resp=msg.message(str(e))
                    
    return(str(msg))

if __name__=="__main__":
    apbot.run(port=5000)