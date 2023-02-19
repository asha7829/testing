'''
Created on 15-Feb-2023

@author: Asha
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
bedsheet= driver.find_element(By.XPATH,"//img[@class='landscape-image' and @alt='Up to 50% off | Comforters & more']")
bedsheet.click()



#send_keys("mobile")

#identify the icon
#click
