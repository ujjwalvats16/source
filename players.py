import requests
import bs4
import io
import lxml
import re

data=requests.get("http://www.espncricinfo.com/ci/content/player/index.html")
#print(type(data))
data=bs4.BeautifulSoup(data.text,"lxml")
#print(type(data))
mainurl="http://www.espncricinfo.com/ci/content/player/caps.html?country="
total=data.select(".ciPlayersHomeCtryList")
for i in total:
    teams=i.find_all("a")
    
    #===========================================================================
    # print(teams[1])
    # x=teams[1].text
    # print(x)
    #===========================================================================
    #===========================================================================
    
    
count=len(teams)
for j in range(count):
    url=teams[j].get("href")
    #print(url)
    url=re.split("=",url)
    url1=mainurl+url[1]+";class=1"
    teamname=teams[j].text
    teamdata=requests.get(url1)
    teamdata=bs4.BeautifulSoup(teamdata.text,"lxml")
    playerdata=teamdata.select(".ciPlayerbycapstable")
    with io.open(teamname +".csv","w",encoding="utf8") as f1:
                f1.write("TAEMNAME,NUMBER,NAME,DEBUTDATE \n")
                f1.close()
    print(len(playerdata))
    for k in playerdata:
        playerstats=k.find_all("li",class_="sep")
        for m in playerstats:
            number=m.find_all("li",class_="ciPlayerbycapstable")
            if(len(number)<1):
                number=m.find_all("li",class_="ciPlayerserialno")
                name=m.find_all("li",class_="ciPlayername")
                #print(name[0].text)
                debutdate=m.find_all("li",class_="ciPlayerplayed")
                #print(debutdate[0].text)
                dataline=teamname + "," + number[0].text + "," + name[0].text + "," + debutdate[0].text
                with io.open(teamname +".csv","a",encoding="utf8") as f1:
                 f1.write(dataline + "\n")
                 f1.close()
                
print("done")
                
            
    
    
    #print(url1)
    
    