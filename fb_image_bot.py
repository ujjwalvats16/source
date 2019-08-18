import requests
import selenium
import re
import json
import time
import io
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL.Image import WEB
import autoit
#from Demos.security.sspi.validate_password import password

#credential to load the username and password
with open("credential.csv") as f1:
    csvrow=csv.reader(f1,delimiter=",")
    for row in csvrow:
        userid=row[0]
        pwd=row[1]
        
#initialization of chrome web driver for selenium
options=webdriver.ChromeOptions()
options.headless=False
prefs={"profile.default_content_setting_values.notifications":2}
options.add_experimental_option('prefs', prefs)
driver=webdriver.Chrome(executable_path="C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe",chrome_options=options)
driver.maximize_window()
driver.get("https://www.facebook.com")

#login from above credential
driver.find_element_by_xpath("//input[@type='email']").send_keys(userid)
driver.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(5)
#select friens chat window and open
driver.find_elements_by_xpath("//li[@class='_42fz']")[0].click()
actions=ActionChains(driver)
time.sleep(5)
actions.send_keys("by selenium").perform()



e=driver.find_element_by_xpath("//div[@data-testid='photo_upload_button']")
actions=ActionChains(driver)
time.sleep(5)
actions.move_to_element(e).send_keys_to_element(e).perform()


#handling windows
#install pyautoit 
#import autoit

time.sleep(10)

autoit.control_focus("Open","")
autoit.control_set_text("Open", "Edit1", "D:\logo2.jpg")
autoit.control_click("Open", "Button1")

time.sleep(6)

driver.find_element_by_xpath("//a[@label='send']").click()











