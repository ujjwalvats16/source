#tutorial 10
#read media attachment and respond with the same media
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import io
import requests
import shutil

apbot=Flask(__name__)
@apbot.route("/sms",methods=["GET","POST"])
def reply():
    #with io.open("media_url.txt","a",encoding="utf-8")as f1:
        #url=[]
    num=request.form.get("From")
    num=num.replace("whatsapp:","")
    msg_text=request.form.get("Body")
    media_url=request.form.get("MediaUrl0")
    file_name=media_url.split("/")[-1]
    read_data=requests.get(media_url,stream=True)
    read_data.raw.decode=True
    
    with open(file_name+".jpg","wb") as f2:
        shutil.copyfileobj(read_data.raw, f2)
        f2.close()
    #url.append(media_url)
    msg=MessagingResponse()
    resp=msg.message("this image sent by "+num)
    resp.media(media_url)
    #f1.write(url[0]+"\n")   
    return(str(msg))
    
       
if __name__=="__main__":
    apbot.run()
    