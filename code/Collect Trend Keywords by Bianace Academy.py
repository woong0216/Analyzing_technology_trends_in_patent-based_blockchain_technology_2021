# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:56:42 2021

@author: Han Jae Woong
"""

# Chrome driver

import pandas as pd
import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver = webdriver.Chrome('chromedriver.exe')  


url="https://academy.binance.com/blockchain/mining-pools-explained" # Cite Address
driver.get(url)

resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")         

while True:

    # Scroll down to bottom                                                      
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)                                                
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")  
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height            
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:                                                
        break

    last_height = new_height
    
# Re-Parsing
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

# Collect Title & Description
titles = []
for title in soup.findAll('div', {'class':'articleContent'}):
    titles.append(title)
    
title=[]
for item in titles:
    new_title = item.find('h1').getText()
    title.append(new_title)    
    
contents = []
for content in soup.findAll('div',{'class':'fr-view'}):
    contents.append(content)
    
content=[]
for item in contents:
    new_content = item.getText()
    content.append(new_content)    
    
# Save DataFrame
dict = {'title':title, 'content':content}
df_dict = pd.DataFrame(dict)
df_dict.to_excel('Trend_keywords.xlsx')
















