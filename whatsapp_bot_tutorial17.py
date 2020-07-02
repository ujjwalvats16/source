from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
import urllib
import csv
from datetime import datetime
import random
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


with open("cred.txt")as f1:
    datarow=csv.reader(f1,delimiter=",")
    for row in datarow:
        id=row[0]
        pwd=row[1]
        
def send_mail(mail,otp):
    sender_mail="ronidas071@gmail.com"
    receiver_email=mail
    password=pwd
    message=MIMEMultipart("alternative")
    message["Subject"]="Urgent:otp from Total Technology"
    message["From"]=sender_mail
    message["To"]=receiver_email
    text=f"""\
Hi,how are you,
 please use otp {otp} for mail validation to complete the registration process."""
    body=MIMEText(text,"plain")
    message.attach(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
        server.login(sender_mail,password)
        server.sendmail(sender_mail,receiver_email,message.as_string())
       
        
client=MongoClient("mongodb+srv://"+id+":"+urllib.parse.quote(pwd)+"@cluster0-lymvb.mongodb.net/<dbname>?retryWrites=true&w=majority")
db=client["whatsapp_db"]
collection=db["users"]
apbot=Flask(__name__)
@apbot.route("/sms", methods=["get","post"])
def reply():
    num=request.form.get("From")
    num=num.replace("whatsapp:","")
    msg_text=request.form.get("Body")
    msg=MessagingResponse()
    x=collection.find_one({"NUMBER":num})
    if(x==None):
        collection.insert_one({"NUMBER":num,"status":"new"})
        resp=msg.message("It seems you are new to our platform ,would you like to register with us, please reply with *yes* or *no*")
    else:
        if(x["status"]=="new"):
            if(msg_text.lower()=="yes"):
                collection.update_one({"NUMBER":num},{"$set":{"status":"input","last":datetime.now().timestamp()}})
                resp=msg.message("""*Please enter you Name & Email address separated by comma*\n ,*For example if your name is john and email address is john@example.com,then you should write john,john@example.com*""")
            
        
            elif(msg_text.lower()=="no"):
                resp=msg.message("""*You must register , at this moment only register user can proceed*""")
                
                
            else:
                resp=msg.message("""*Invalid input , please enter yes or no*""")
                
            
        if(x["status"]=="input"):
            try:
                user_input=msg_text.split(",")
                otp=random.randint(0000,9999)
                name=user_input[0]
                mail=user_input[1]
                send_mail(mail,otp)
                resp=msg.message(f"We have sent otp to {mail}")
                collection.update_one({"NUMBER":num},{"$set":{"NAME":name,"EMAIL":mail,"OTP":otp,"status":"added","last":datetime.now().timestamp()}}) 
            except Exception as e:
                if (str(e)=="list index out of range"):
                 resp=msg.message("*You have not entered youe name and mail address properly , please use comma to separte the name and email address*") 
                else:
                    resp=msg.message(str(e))
                
                
                 
    
   
    
    return(str(msg))

if __name__=="__main__":
    apbot.run(port=5000)