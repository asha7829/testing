"""from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S906507790%3A1675601347451743&authuser=0&continue=https%3A%2F%2Fmail.google.com&ec=GAlAFw&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")
#driver.find_element(By.NAME,"q").send_keys("mantralayam")
#driver.find_element(By.LINK_TEXT,"Gmail").click()
#driver.find_element(By.LINK_TEXT,"For work").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"For w").click()
#driver.find_element(By.LINK_TEXT,"Sign in").click()
#driver.find_element(By.LINK_TEXT,"About").click()
#link=driver.find_elements(By.TAG_NAME,"a")
#print(len(link))
#driver.find_element(By.ID,"twotabsearchtextbox").send_keys("baby toys")
#driver.find_element(By.LINK_TEXT,"Visit the store").click()
#link=driver.find_elements(By.TAG_NAME,"a")
#print(len(link))
#slider=driver.find_elements(By.CLASS_NAME,"hmenu-separator")
#print(len(slider))
#driver.find_element(By.LINK_TEXT,"Best Sellers").click()
#CSS selector

#driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox").send_keys("Home decoration")
#driver.find_element(By.CSS_SELECTOR,"input.nav-input").send_keys("Electronics")
#driver.find_element(By.CSS_SELECTOR,"input[type=submit]").send_keys("go")
#driver.find_element(By.CSS_SELECTOR,"input.whsOnd[name=ConfirmPasswd]").send_keys("asha@")
driver.maximize_window()
slidder=driver.find_elements(By.CLASS_NAME,"G3hhxb")
print(len(slidder))"""


"""
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://snapdeal.com")
driver.maximize_window()
driver.find_element(By.ID,"inputValEnter").send_keys("Kurta Sets")
driver.find_element(By.LINK_TEXT,"Impact@Snapdeal").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Gif").click()
link=driver.find_elements(By.TAG_NAME,"a")
print(len(link))
driver.find_elements(By.CLASS_NAME,"navlink")"""

"""
from selenium import webdriver
#from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.firstcry.com/")
driver.maximize_window()
#driver.find_element(By.ID,"search_box").send_keys("  BOY FASHION")
#link=driver.find_elements(By.TAG_NAME,"a")
#print(len(link))
#slidder=driver.find_elements(By.CLASS_NAME,"M14_42 categry")
#print(len(slidder))


#Absolute:
#/html/body/div[1]/header/div/div[1]/div[1]/div[1]/a

#/html/body/div[1]/header/div/div[1]/div[1]/div[2]/span

#Relative:
#//*[@id="nav-logo-sprites"]

#//*[@id="nav-global-location-data-modal-action"]

from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.firstcry.com/")
driver.maximize_window()
#driver.find_element(By.ID,"search_box").send_keys("  BOY FASHION")
#link=driver.find_elements(By.TAG_NAME,"a")
#print(len(link))
slidder=driver.find_elements(By.CLASS_NAME,"M14_42 categry")
print(len(slidder))


#most of the project we use relative xpath.
#Absolute:
#/html/body/div[1]/header/div/div[1]/div[1]/div[1]/a

#/html/body/div[1]/header/div/div[1]/div[1]/div[2]/span

#Relative:
#//*[@id="nav-logo-sprites"]

#//*[@id="nav-global-location-data-modal-action"]"""

"""
from selenium import webdriver  
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("Mobiles")
#driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()
driver.find_element(By.XPATH,"//*[@id='nav-xshop']/a[2]").click()
"""