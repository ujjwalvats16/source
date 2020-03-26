import requests
import json


def get_data(msg_text):
 url = "https://covid-193.p.rapidapi.com/statistics"
 headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "7d18fd6581msh81a4886d454a322p1e64c5jsn2c784c87b0cf"
    }

 response = requests.request("GET", url, headers=headers)
 data=response.text
 data=json.loads(data)
 for i in range(len(data["response"])):
    x=data["response"][i]["country"]
    if(x.lower()==msg_text.lower()):
        total=data["response"][i]["cases"]["total"]
        active_cases=data["response"][i]["cases"]["active"]
        recovered=data["response"][i]["cases"]["recovered"]
        critical_cases=data["response"][i]["cases"]["critical"]
        new_cases=data["response"][i]["cases"]["new"]
        total_deaths=data["response"][i]["deaths"]["total"]
        new_deaths=data["response"][i]["deaths"]["new"]
        data_complete="""total_infectd: """+str(total)+"""
active_case: """+str(active_cases)+"""
recovered: """+str(recovered)+"""
critical_cases: """+str(critical_cases)+"""    
new_cases: """+str(new_cases)+"""
tota_death: """+str(total_deaths)+"""
new_deaths: """+str(new_deaths) 
        return(data_complete)
        break 
     
 return("country entered not found")    
