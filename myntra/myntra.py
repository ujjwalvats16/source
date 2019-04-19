import wsurlopen 
import bs4
import lxml
import re
import io
import pandas as pd
import time,datetime
from _operator import index

var=wsurlopen.urlopen('https://www.myntra.com/amp/men-tshirts') 
read=bs4.BeautifulSoup(var.text,"lxml") 
#print(read)
count=read.select(".index-productCount")
counter=count[0].getText()
print(counter)

counter=(re.sub("styles", "",counter)).strip()
print(counter)
counter=int(counter)//500
print(counter)
with io.open("file1.csv","w",encoding="utf8") as f1:
    f1.write("BRAND,PRODUCT,CURRENT PRICE,OLD PRICE,DISCOUNT\n")
with io.open("file2.csv","w",encoding="utf8") as f2:
    f2.write("lINK\n")    
    
i=0
for i in range(int(counter)+1):
    i=i+1
    url1="https://www.myntra.com/amp/men-tshirts?rows=500&p"
    url1=url1+"p="+str(i)
    var1=wsurlopen.urlopen(url1)
    readfull=bs4.BeautifulSoup(var1.text,"lxml")
    read1=readfull.select(".productInfo")
    read2=readfull.select(".product")
    #print(read1)
    #print(read2)
    for j in read1:
        name=j.select(".name")
        name=name[0].getText()
        
        itemname=j.select(".name-product")
        itemname=itemname[0].getText()
        
        ap=j.select(".price-discounted")
        ap=ap[0].getText()
        ap=ap[1:]
        
        dp=j.select(".price")
        #dp=dp[0].text
        if(len(dp)>0):
            dp=dp[0].text
        else:
            dp=ap 
            
               
        dis=j.select(".price-discount")
        #dp=dp[0].text
        if(len(dis)>0):
            dis=dis[0].text
        else:
            dis="no discount"      
        
        data=name + "," + itemname + "," + ap + "," + dp + "," + dis + "\n"
        with io.open("file1.csv","a",encoding="utf8") as f1:
            f1.write(data)
            f1.close()
        
    for k in read2:
        link=k.a["href"]
        link="https://www.myntra.com/tshirts/" + link
        data1=link+"\n"
        with io.open("file2.csv","a",encoding="utf8") as f2:
            f2.write(data1)
            f2.close()
        
        
    
        #=======================================================================
        # print(name,end=",")
        # print(itemname,end=",")
   # print(dp,end=",")
        # print(dis)
        #=======================================================================
df1=pd.read_csv("file1.csv") 
df2=pd.read_csv("file2.csv")  
merged=df1.join(df2)
timedatev=time.strftime("%Y%m%d --%H%M%S")
merged.to_csv(timedatev + ".csv",index=False)
print("done")
    

#https://www.myntra.com/amp/men-tshirts?rows=500&p=4
