from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import datetime

apbot=Flask(__name__)
@apbot.route("/sms",methods=["get","post"])
def reply():
    msg_text=request.form.get("Body")
    sen_num=request.form.get("From")
    sen_num=sen_num.replace("whatsapp:","")
    msg=MessagingResponse()
    response=msg.message("you send " +msg_text +" from :"+sen_num)
    response1=msg.message("total technology logolaslaSLakslaSLAksas")
    response1.media("http://71d67779.ngrok.io/Users/roni/eclipse-workspace/watsappbot/w.jpg")
    return(str(msg))
    
    
    
    
    
    
if (__name__=="__main__"):
 apbot.run()