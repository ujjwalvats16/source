from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import csv 
import re
import io
import sys
import datetime
import os
sys.stdout.reconfigure(encoding='utf-8')



with open("credential.csv") as f1:
    csvrow=csv.reader(f1,delimiter=",")
    for row in csvrow:
     email=row[0]
     pswd=row[1]


options=webdriver.ChromeOptions()

roni={"profile.default_content_setting_values.notifications":2}
options.add_experimental_option("prefs",roni)
driver=webdriver.Chrome(executable_path="/Users/roni/eclipse-workspace/youtube/chromedriver2",chrome_options=options)
time.sleep(3)
driver.maximize_window()
driver.get("https://twitter.com/login")
driver.find_element_by_xpath('//input[@placeholder="Phone, email or username"]').send_keys(email)
driver.find_element_by_xpath('//input[@class="js-password-field"]').send_keys(pswd)
driver.find_element_by_xpath('//input[@class="js-password-field"]').send_keys(Keys.RETURN)
time.sleep(3)
driver.get("https://twitter.com/search?f=tweets&vertical=news&q=%23Matplotlib&src=tyah")

time.sleep(5)
for i in range(1000):
    
 driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
 
 time.sleep(3)
elements=driver.find_elements_by_class_name("tweet")
print(len(elements))


    
tweets=[element.get_attribute("data-permalink-path") for element in elements]  
 

print(tweets)

new_tweets=[]
for xi in tweets[:-1] :
    if (("/supratim_sur/status") not in xi):
        #print(xi)
        new_tweets.append(xi)

with io.open("latest.csv","r",encoding="utf-8")as f1:
    lasttweetid=f1.read()
    f1.close()

if not os.path.exists('machinelearning'):
         os.mkdir('machinelearning')
          
with io.open(os.getcwd()+'/' + 'machinelearning' + '/' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + "_tweets.csv","a",encoding="utf-8")as f1:
    f1.write('profile'+','+'tweetlinks'+'\n')
     
     
             
    for tweet in new_tweets:
        data=''
        linkold="https://twitter.com" + lasttweetid
        linknew="https://twitter.com" + tweet
        profilenumber=tweet.split('status')[1]
        profilenumber=profilenumber.replace('/','')
        if(linkold==linknew):
            break
        driver.switch_to.active_element
        driver.get(linknew)  
        driver.switch_to.active_element
        time.sleep(3)
 
          
         
         
        driver.find_element_by_id("tweet-box-reply-to-" + profilenumber).click()
        driver.find_element_by_id("tweet-box-reply-to-" + profilenumber).click()
        driver.find_element_by_id("tweet-box-reply-to-" + profilenumber).send_keys('Step by step and detailed tutorial on #matplotlib, https://www.youtube.com/watch?v=frPl-a2W6d8&list=PLI8raxzYtfGxG1TGMbsah7zcZZIq_HFfw')
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.find_elements_by_xpath("//span[contains(text(),'Reply') and @class='button-text replying-text']")[-2].click()
        
    
         
         
        
        s="https://twitter.com" + tweet
        s=s.split("https://twitter.com/")
        s=s[1]
        s=s.split('/status')[0]
        element=driver.find_element_by_xpath("//div[@class='js-tweet-text-container']")
        x=element.text
        ss="machinelearning\\"+s
        if not os.path.exists(ss):
         os.makedirs(ss)
     
         with io.open(os.getcwd()+'/' + ss + '/' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '_'+ profilenumber + '.txt','a',encoding='utf-8') as f2:
             f2.write('tweet link is:\n')
             f2.write('\n')
             f2.write(tweet+'\n')
             f2.write('\n')
             f2.write('tweet content is:\n')
             f2.write('\n')
             f2.write(x+'\n')
              
             f2.close()
         
        data=s+','+ 'https://twitter.com' + tweet+'\n'
        f1.write(data)
         
        time.sleep(3) 
         
 
         
         
         
   
    f1.close()
print(new_tweets[0])    
    
with io.open("latest.csv","w",encoding="utf-8")as f1:
    tweets[0]
    f1.write(new_tweets[0])
    f1.close()
new_tweets[0]        
driver.close()
