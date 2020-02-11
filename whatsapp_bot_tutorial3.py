#flask,twilio & reportlab
#tutorial 3
#how to send pdf file using whatsapp bot

from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm


appbot=Flask(__name__)
@appbot.route("/sms",methods=["GET","POST"])
def reply():
    pdf=canvas.Canvas("whatsapp.pdf")
    num=request.form.get("From")
    num=num.replace("whatsapp:","")
    msg_text=request.form.get("Body")
    dt=datetime.datetime.now().strftime("%y%m%d--%H%M%S")
    text="you sent " + msg_text + " from "+num + " at " +dt
    pdf.drawString(100,600,text)
    pdf.save()
    print(text)
    msg=MessagingResponse()
    resp_text=msg.message("the message you sent is in the attached file")
    resp_text.media( "http://b5681af8.ngrok.io/Users/roni/eclipse-workspace/watsappbot/whatsapp.pdf")
    return(str(msg))
    
    
if __name__=="__main__" :
    appbot.run()