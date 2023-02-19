'''
Created on 19-Feb-2023

@author: Asha
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
#import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://amzn.to/3Ejx2VR")
driver.maximize_window()
#image=driver.find_element(By.XPATH,"(.//*[contains(@src,'81UT07JsBqL._SL1500_.jpg')])[2]")
img=driver.find_element(By.XPATH,".//img[@id='landingImage']")
action=ActionChains(driver)
action.move_to_element(img).perform()
