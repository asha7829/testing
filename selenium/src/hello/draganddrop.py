'''
Created on 18-Feb-2023

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
driver.switch_to.parent_frame()
source=driver.find_element(By.XPATH,"//div[@id='draggable']")
target=driver.find_element(By.XPATH,"//div[@id='droppable']")
action=ActionChains(driver)
action.drag_and_drop_by_offset(source, 150, 50).perform()
#action.drag_and_drop(source, target).perform()
print(source.get_attribute("id"))
action.drag_and_drop_by_offset(source, 150, 50).perform()
#action.drag_and_drop(source, target).perform()
print(source.get_attribute("id"))


click_me=driver.find_element(By.XPATH,".//input[@id='field2']")
action=ActionChains(driver)
action.double_click(click_me).perform()