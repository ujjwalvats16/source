#pip install flask
#pip install twilio
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
apbot=Flask(__name__)
@apbot.route("/sms", methods=["GET","POST"])
def reply():
    num=request.form.get("From").replace("whatsapp:","")
    msg_text=request.form.get("Body")
    num_media=request.form.get("NumMedia")
    print(request.form)
    if(num_media=="1"):
        type=request.form.get("MediaContentType0")
        if(type.split("/")[1]=="csv"):
        
          msg=MessagingResponse()
          resp=msg.message(f"you send {msg_text} from {num},and you send csv attachment")
          return(str(msg))         
        else:
            file_type=type.split("/")[1]
            msg=MessagingResponse()
            resp=msg.message(f"you send {msg_text} from {num} , but your attachment is in {file_type},which is invalid ")
            return(str(msg))
    else:
        msg=MessagingResponse()
        resp=msg.message(f"you have not attached any file send from {num}")
        return(str(msg))
        
if __name__=="__main__":
    apbot.run(port=5000)
