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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#alertPOOP=driver.find_element(By.XPATH,".//button[@onclick='myFunction()']")
# alertPOOP.click()
# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()
# textVALUE=driver.find_element(By.XPATH,".//p[@id='demo']")
# print(textVALUE.text)
# print(textVALUE.text)
# driver.switch_to.frame("frame-one1434677811")
# send_KEYS=driver.find_element(By.XPATH,".//input[@name='RESULT_TextField-1']")
# send_KEYS.send_keys("abc@gmail.com")
# driver.find_element(By.XPATH,".//input[@name='RESULT_RadioButton-7' and @id='RESULT_RadioButton-7_0']")
# radio_BUTTON=driver.find_element(By.XPATH,"//label[@for='RESULT_RadioButton-7_0']")
# radio_BUTTON.click()
# driver.switch_to.parent_frame()
# driver.find_element(By.XPATH,".//label[@for='speed']")
# select_Box=driver.find_element(By.XPATH,".//select[@name='speed']")
# select_Box.click()
# select_Box.send_keys("Medium")
# select_Box.click()
driver.switch_to.frame("frame-one1434677811")
weeks=driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-8_0']")
driver.execute_script("arguments[0].scrollIntoView();",weeks)  #scrolling webpage
weeks.click()
  
