#twilio whatsapp bot 

from flask import Flask,request,send_file
from twilio.twiml.messaging_response import MessagingResponse
import io
import datetime



appbot=Flask(__name__)
@appbot.route("/sms", methods=["get","post"])
def reply():
    with io.open("response.csv","a",encoding="utf-8")as f1:
        ur=request.form.get("Body")
        un=request.form.get("From")
        un=un.replace("whatsapp:","")
        dt=datetime.datetime.now().strftime("%y%m%d--%H%M%S")
        data=un+","+ur+","+dt+"\n"
        print(un)
        f1.write(data)
        resp=MessagingResponse()
        msg=resp.message("you sent"+" "+ur+" "+"from"+" "+un+" "+"on"+" "+dt)
        return(str(resp))
        
    
    f1.close()
if (__name__=="__main__"):
 appbot.run()  
    