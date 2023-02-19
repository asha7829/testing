'''
Created on 17-Jan-2023

@author: Asha
'''
"""
from selenium import webdriver
#from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.firstcry.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)"""

from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.redbus.in/bus-tickets")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
#print(driver.page_source)
#search_box=driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']")
#print(search_box.is_displayed())

#search_box=driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']")
#print(search_box.is_enabled())

date=driver.find_element(By.XPATH,"//*[@id='txtOnwardCalendar']")
print(date.is_enabled())
