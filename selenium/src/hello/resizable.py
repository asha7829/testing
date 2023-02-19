'''
Created on 19-Feb-2023

@author: Asha
'''
from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
#driver.get("http://www.google.com")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()