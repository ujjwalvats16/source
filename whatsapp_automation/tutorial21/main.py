import csv
from pymongo import MongoClient
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import json
import urllib
from pymongo.mongo_client import MongoClient
from fetchdata import get_data
from report_pdf import gen_pdf


with open("cred.txt")as f1:
    datarow=csv.reader(f1,delimiter=",")
    for row in datarow:
        user_id=row[0]
        pwd=row[1]
client=MongoClient("mongodb+srv://"+user_id+":"+urllib.parse.quote(pwd)+"@cluster0.lymvb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client["whatsapp_db"]
collection=db["whatsapp_db"]

app=Flask(__name__)
@app.route("/sms",methods=["GET","POST"])
def reply():
    num=request.form.get("From")
    num=num.replace("whatsapp:","")
    print(num)
    msg_text=request.form.get("Body")
    if "," in msg_text:
        pin=msg_text.split(",")[0]
        date=msg_text.split(",")[1]
        x=collection.find_one({"NUMBER":num})
        try:
           status=x["status"]
        except:
            pass
        if(bool(x)==False):
            collection.insert_one({"NUMBER":num,"status":"first"})
            msg=MessagingResponse()
            resp=msg.message("""Hello this is T2 from total technology,developed by roni , to get covid vaccine availability related informaion please follow the below
enter your pincode and date separated by comma , for example if your pincode is 1100045 and date you want for 15 th may 2021 , then your input should be 
1100045,15-05-2021""")
            return (str(msg))
        else:
            if (status=="first"):
                data=get_data(pin,date)
                msg=MessagingResponse()
                
                if (data=="invalid pincode"):
                    resp=msg.message("please entre valid pincode")
                    return (str(msg))
                elif (data=="no centre"):
                    resp=msg.message("no centre found for your given input ,please try again later or else try with find with nearest pincode")
                    return (str(msg))
                else:
                    if(len(data)<15):
                        parse_data=json.dumps(data)
                        parse_data=parse_data.replace("{","")
                        parse_data=parse_data.replace("}","\n\n")
                        parse_data=parse_data.replace("[","")
                        parse_data=parse_data.replace("]","")
                        parse_data=parse_data.replace(",","\n")
                        resp=msg.message(parse_data)
                        #print(parse_data)
                        return (str(msg))
                    else:
                        print("abc")
                        resp1=msg.message("please fid the pdf for more information")
                        gen_pdf(num,data)
                        resp1.media("http://48261c041578.ngrok.io/Users/roni/eclipse-workspace/VACCINE_PROJECT/"+num+".pdf")
                        return(str(msg))
                
    
    else:
        msg=MessagingResponse()
        resp=msg.message("""invalid input , to get covid vaccine availability related informaion please follow the below
enter your pincode and date separated by comma , for example if your pincode is 1100045 and date you want for 15 th may 2021 , then your input should be 
1100045,15-05-2021""")
        return (str(msg))
        
        print(num)
    
#https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=110001&date=31-03-2021

#headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
if __name__=="__main__":
    app.run(port=5000)