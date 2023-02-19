'''
Created on 15-Feb-2023

@author: Asha
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
#driver.get("https://www.amazon.in/")
driver.get("https://www.flipkart.com/")
driver.maximize_window()
#mobile=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
#mobile.send_keys("Mobiles")
#=driver.find_element(By.XPATH,".//input[@type='submit']")
#send.click()
mobile=driver.find_element(By.XPATH,".//input[@class='_3704LK']")
driver.find_element(By.XPATH,".//button[@class='_2KpZ6l _2doB4z']").click()
mobile.send_keys("baby")
driver.find_element(By.XPATH,"//a[@class='_1_3w1N']").click()
#driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']").click()
#driver.find_element(By.XPATH,".//button[@class='L0Z3Pu']").click()
