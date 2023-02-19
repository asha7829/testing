'''
Created on 07-Jan-2023

@author: Asha
'''
print("hello world")

#test case
from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome("C:\\Users\\Asha\\Downloads\\chromedriver_win32\\chromedriver.exe")
# to maximize the browser window
#driver.maximize_window()
#get method to launch the URL
driver.get("https://www.gmail.com/")

"""we want automate these steps the first and most imp step is we need import webdriver module 
actually webdriver is module mutliple class are creted that is chrome(),firefox(), edge()
webdriver is one of the component in selenium package installed
webdriver is having class and methods functions"""

"""from webdriver module we need class chrome there is a constructor() browser driver as parameter along with name of the file chromedriver.exe"""

"""there are 2 type of arguments in python
postional arguments
keyword arguments(executable_path)"""

"""first step:
open the webdriver (chrome)
second step
open url https://www.gmail.com/

selenium 3 DependencyWarning will not come
selenium 4 DependencyWarning will come (means in future version they will remove)

*)web page is having web element image,text box,button,link"""
#driver is object of chrome class

#test case
from selenium.webdriver.chrome.service import Service
obj=Service("C:\\Users\\Asha\\Downloads\\chromedriver_win32\\chromedriver.exe")
#from selenium import webdriver
from selenium.webdriver.common.by import By
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
#driver=webdriver.Chrome()
driver = webdriver.Chrome(service=obj)
# to maximize the browser window
#driver.maximize_window()
#get method to launch the URL    
driver.get("https://www.gmail.com")
#driver.find_element(By.NAME,"identifier").send_keys("email")
driver.find_element(By.ID,"identifierId").send_keys("phone number")