'''
Created on 19-Feb-2023

@author: Asha
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
#import time
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
#driver.get("http://www.google.com")
driver.get("https://testautomationpractice.blogspot.com/")
click_me=driver.find_element(By.XPATH,".//button[@ondblclick='myFunction1()']")
#click_me.send_keys("Hello World!")
action=ActionChains(driver)
action.double_click(click_me).perform()