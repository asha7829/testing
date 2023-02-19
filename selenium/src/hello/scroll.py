'''
Created on 18-Feb-2023

@author: Asha
'''
from selenium import webdriver
#from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
time.sleep(7)
driver.execute_script("window.scrollBy(0,600)","")
driver.close()