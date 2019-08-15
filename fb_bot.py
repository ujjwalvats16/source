import requests
import json
import selenium
import time
import re
import io
import csv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

with open("credentital.csv") as f1:
    csvrow=csv.reader(f1,delimiter=",")
    for row in csvrow:
        userid=row[0]
        pwd=row[1]
    
    
options=webdriver.ChromeOptions()
options.headless=False

prefs={"profile.default_content_setting_values.notifications":2}
options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome("/Users/roni/eclipse-workspace/youtube/chromedriver-3",chrome_options=options)
driver.maximize_window()
driver.get("https://www.facebook.com")
time.sleep(5)

driver.find_element_by_id("email").send_keys(userid)
driver.find_element_by_id("pass").send_keys(pwd)
driver.find_element_by_xpath("//input[@type='submit']").click()  

time.sleep(5)
driver.get("https://www.facebook.com/totaltechnol0gy/")
time.sleep(10)
count=driver.find_element_by_xpath('//*[contains(text()," likes ")]')
print(count.text)
count=(count.text).split("likes")
count=count[0].strip()
count=count.replace(",","")
driver.close()

headers = {
    'origin': 'https://www.facebook.com',
    #'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'referer': 'https://www.facebook.com/totaltechnol0gy/settings/?tab=people_and_other_pages',
    'authority': 'www.facebook.com',
    'cookie': 'datr=Se-nXHgIACChttjGwE5XUYcp; sb=Se-nXMQaq6GeXTLSYzc0qc0s; c_user=100001255898953; xs=21%3AqfVhISHOZZwCsg%3A2%3A1554509653%3A19060%3A4248; spin=r.1000574873_b.trunk_t.1554509653_s.1_v.2_; fr=1qH94jDkD8UofV2Nn.AWV_WdhAR5U9ZDewr2N_SuxbpVw.Bcp-9J.Ru.Fyn.0.0.Bcp-9g.AWXDsOz4; act=1554509733997%2F3; wd=1440x316; presence=EDvF3EtimeF1554509880EuserFA21B01255898953A2EstateFDutF1554509880798CEchFDp_5f1B01255898953F3CC',
}

params = (
    ('query_edge_key', 'PEOPLE_WHO_LIKE_THIS_PAGE'),
    ('page_id', '2459218040755894'),
    ('offset', '0'),
    ('limit', int(count)),
)

data = {
  '__user': '100001255898953',
  '__a': '1',
  '__dyn': '7AgNe-4amaWxd2u5bGSF8CC5EWq2W8GAdyeGDiheCGgjCx-6ES2N6xvyd7yWCHxvG4VEG49FGwwz8yGDyUJu9x2axnGi4FpenK7GgPwExaF-58-ENyKi8yU-4p94jUCjVoS48pDAyF8OESq5o8Ua9ohGVoyaDzp8hz8faxlem6uK4bh43GF8GdzVK5e9g9p44UlDBgS6ojzoSaCCy8K6pEhKFprzooAnyrUpCyqkxteE_-dCz5p4mfxFebKqifyoPKiFE-1dx3xiGzXHQbALwyzV5zEK4uey9oOjyEaLKfBzAhxfyopAx3yBz9rBKuuejzK2iazUCbryU8Ey6GwBxmqhoyV9-p6Ki8xWbx2ieAyHGfwOgigJ7GmuEmy8hGHxq48gzFCcKfF2Uy58OidmaybhbyUOby8C6o9rxidwAxGEyUkU',
  '__req': '2b',
  '__be': '1',
  '__pc': 'PHASED:ufi_home_page_pkg',
  'dpr': '1',
  '__rev': '1000574873',
  '__comet_req': 'false',
  'fb_dtsg': 'AQFnIY-5pBqH:AQFZKAD5R2So',
  'jazoest': '21900',
  '__spin_r': '1000574873',
  '__spin_b': 'trunk',
  '__spin_t': '1554509653'
}

response = requests.post('https://www.facebook.com/pages/admin/people_and_other_pages/entquery/', headers=headers, params=params, data=data)
#print(response.text)
data=response.text
data=data.replace("for (;;);","",1)
print(data)
data1=json.loads(data)
datafull=data1["payload"]["data"]
print(datafull)
l1=[]
l1.append(datafull)
with io.open("members.txt","a",encoding="utf8")as f1:
    f1.write("name,link\n")
    f1.close()

def memwrite(list1): 
    with io.open("members.txt","a",encoding="utf8")as f1:
        for i in range(len(list1)):
            name=list1[i]["profile"]["name"] 
            link=list1[i]["profile"]["id"] 
            dataline=str(name)+",https://facebook.com/"+str(link)+"\n"
            f1.write(dataline)
        f1.close()    
    

for k in range(len(l1)):
    memwrite(l1[k])

options=webdriver.ChromeOptions()
options.headless=False

prefs={"profile.default_content_setting_values.notifications":2}
options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome("/Users/roni/eclipse-workspace/youtube/chromedriver-1",chrome_options=options)
driver.maximize_window()
driver.get("https://www.facebook.com")
time.sleep(5)
driver.find_element_by_id("email").send_keys(userid)
driver.find_element_by_id("pass").send_keys(pwd)
driver.find_element_by_xpath("//input[@type='submit']").click()  
time.sleep(5)

with io.open("members.txt") as f2:
    csvrow=csv.reader(f2,delimiter=",")
    line=0
    for row in csvrow:
        if (line>0):
            link=row[1]
            
            driver.get(link)
            time.sleep(3)
            driver.find_element_by_xpath('//a[text()="Message"]').click()
            time.sleep(3)
            e=driver.find_elements_by_xpath("//*[@data-editor]")
            if(len(e)>1):
                name=row[0]
                e[1].click()
                actions=ActionChains(driver)
                actions.send_keys(f"hi{name}")
                actions.send_keys(Keys.ENTER)
                actions.perform()
                time.sleep(3)
                driver.get("https://www.facebook.com")
                time.sleep(3) 
                #===============================================================
                # alert=driver.switch_to_alert()
                # alert.accept()
                #===============================================================
                
            else:
                link=row[1]
                name=row[0]
                e[0].click()
                actions=ActionChains(driver)
                actions.send_keys(f"hi{name}")
                actions.send_keys(Keys.ENTER)
                actions.perform() 
                time.sleep(3)
                driver.get("https://www.facebook.com") 
                time.sleep(3)
                #===============================================================
                # alert=driver.switch_to_alert()
                # alert.accept()  
                #===============================================================

        line=line+1

   


