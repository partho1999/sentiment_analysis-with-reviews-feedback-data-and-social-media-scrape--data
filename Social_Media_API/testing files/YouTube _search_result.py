import re
import csv 
from getpass import getpass 
from time import sleep 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException 
import os
import selenium
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
from getpass import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


# create instance of Chrome webdriver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('C:/Users/Opus/chromedriver.exe', chrome_options=chrome_options)
text= "covid"
driver.get('https://www.youtube.com/results?search_query='+ text)
contents = driver.find_elements(By.XPATH, '//*[@id="dismissible"]')


duration_lst=[]
title_lst=[]
views_lst=[]
uploaded_lst=[]
channel_lst=[]
description_lst=[]
for content in contents:
    try:
        duration=content.text.split('\n')[0]
        title=content.text.split('\n')[1]
        views=content.text.split('\n')[2]
        uploaded=content.text.split('\n')[3]
        channel=content.text.split('\n')[4]
        description=content.text.split('\n')[5]
    except:
        continue
    duration_lst.append(duration)
    title_lst.append(title)
    views_lst.append(views)
    uploaded_lst.append(uploaded)
    channel_lst.append(channel)
    description_lst.append(description)

df = pd.DataFrame(
    {'Title':title_lst, 
    'Description':description_lst,
    'Duration':duration_lst,
    'Views':views_lst,
    'Channel':channel_lst,
    'Uploaded':uploaded_lst
    })
df.to_csv("youtube.csv", index= False, header= True)