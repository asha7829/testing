'''
Created on 17-Feb-2023

@author: Asha
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
#import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//img[@alt='Helmets']").click()
driver.find_element(By.XPATH,"//img[@alt='Vega Crux Open Face Black Helmet-M']").click()
driver.find_element(By.XPATH,"//a[@id='bylineInfo']").click()