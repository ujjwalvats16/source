# tutorial5
# whatsapp bot to get live status update on corona virus
import csv
from pymongo import MongoClient
from flask import Flask, request, abort, send_file
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

import datetime
import urllib.parse
from corona_plot1 import get_data
import os
import io

# variables added by Joseph

url=""
# region

with io.open("vip.txt", "r", encoding="utf-8") as f1:
    data_vip = f1.read()
    f1.close()

data_vip = data_vip.split("\n")
print(data_vip)
# database setup
with open("cred.txt")as f1:
    datarow = csv.reader(f1, delimiter=",")
    for row in datarow:
        id = row[0]
        pwd = row[1]
        
        
        
        
with open("credentials.txt")as f1:
    datarow = csv.reader(f1, delimiter=",")
    for row in datarow:
        id_tunnel = row[0]
        pwd_tunnel = row[1] 
        url=row[2]
        token=row[3]
        pwd_tunnel=pwd_tunnel.replace("@","xyz")
        
print(url)        
        

       

# endregion
# database connectivity
# region
client = MongoClient("mongodb+srv://" + id + ":" + urllib.parse.quote(
    pwd) + "@cluster0-lymvb.mongodb.net/test?retryWrites=true&w=majority")
db = client["whatsapp_db"]
collection = db["whatsapp_db"]

# endregion#flask part
# region
apbot = Flask(__name__)

def validate(request,url):
    request_meta_data=dict()
    validator=RequestValidator(token)
    print(url)
    url=url+"/"+"sms"
    for key_item in request.form:
         request_meta_data[key_item]=request.form[key_item]
    twilio_signature=request.headers.get("X-Twilio-Signature",None)
    print(twilio_signature)
    print(request_meta_data)
    print(validator.validate(url, request_meta_data, twilio_signature))
    return(validator.validate(url, request_meta_data, twilio_signature))
         
    
    



@apbot.route("/sms", methods=["post"])
def reply():
    is_valid=validate(request,url)
    if not (is_valid):
        abort(403,"request not allowed")
  

    num = request.form.get("From")
    num = num.replace("whatsapp:", "")
    msg_text = request.form.get("Body")

    print(num)
    x = collection.find_one({"NUMBER": num})
    try:
        status = x["status"]
    except:
        pass
    try:
        os.remove(num + ".png")
    except:
        pass
    if (bool(x) == False):
        collection.insert_one({"NUMBER": num, "status": "first"})
        msg = MessagingResponse()
        resp = msg.message('''Hello , myself teetuu , a bot from total technology:
Utilize my services to get live status update on corona virus.
please select from below ,
*To get country specific data enter country name ,for example if you want to get update for australia please enter australia(not case sensitive)*''')
        return (str(msg))
    else:
        if (status == "first"):
            data = get_data(msg_text, num)
            msg = MessagingResponse()
            # msg1=MessagingResponse()
            resp = msg.message(data)
            # collection.delete_one({"NUMBER":num})
            collection.update_one({"NUMBER": num},
                                  {"$set": {"status": "done", "last": datetime.datetime.now().timestamp()}})

            print(data)

            if (data == "country entered not found"):
                print(str(msg))
                return (str(msg))

            else:
                resp1 = msg.message("")
                image_url = "http://"+id_tunnel+":"+pwd_tunnel+"@5da7f075.ngrok.io/"+num+".png"
                print(image_url)
                
                resp1.media(image_url)

                return (str(msg))

        if (status == "done"):
            t1 = x["last"]
            t2 = datetime.datetime.now().timestamp()
            if (num in data_vip):
                msg = MessagingResponse()
                collection.update_one({"NUMBER": num},
                                      {"$set": {"status": "first", "last": datetime.datetime.now().timestamp()}})
                resp = msg.message('''Hello , myself teetuu , a bot from total technology:
Utilize my services to get live status update on corona virus.
please select from below ,
*To get country specific data enter country name ,for example if you want to get update for australia please enter australia(not case sensitive)*''')
                return (str(msg))

            else:
                if ((t2 - t1) > 1800):
                    msg = MessagingResponse()
                    collection.update_one({"NUMBER": num},
                                          {"$set": {"status": "first", "last": datetime.datetime.now().timestamp()}})
                    resp = msg.message('''Hello , myself teetuu , a bot from total technology:
Utilize my services to get live status update on corona virus.
please select from below ,
*To get country specific data enter country name ,for example if you want to get update for australia please enter australia(not case sensitive)*''')
                    return (str(msg))

                else:
                    dif = t2 - t1
                    dif = (1800 - dif)
                    dif = int(dif / 60)
                    msg = MessagingResponse()
                    resp = msg.message(
                        '''You are not allowed to use the bot at this moment , please try again after''' +
                        str(dif) + ''' minutes.
If you want to use vip access code please contact roni@totaltechnology.in''')
                    return (str(msg))


# endregion
if __name__ == "__main__":
    apbot.run(port=5000, debug=True)
