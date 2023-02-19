'''
Created on 18-Feb-2023

@author: Asha
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
#import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
rediffMAIL=driver.find_element(By.XPATH,".//input[@type='submit']")
rediffMAIL.click()
alertWINDOW=driver.switch_to.alert
print(alertWINDOW.text)
alertWINDOW.accept()

