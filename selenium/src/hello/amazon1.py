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
driver.find_element(By.XPATH,"//img[@alt='ACs']").click()
#driver.find_element(By.XPATH,".//img[@src='https://images-eu.ssl-images-amazon.com/images/G/31/img22/Fashion/Gateway/BAU/BTF-Refresh/May/PC_WF/WF1-186-116._SY116_CB636048992_.jpg']").click()
#driver.find_element(By.XPATH,".//*[@class='s-image' and @alt='JUNEBERRY Women Sweatshirt with Hoodies, Fleece Material Full Sleeves Jumper Women Winter Wear, Hooded Neck Regular Fit Lo...']").click()
#driver.find_element(By.XPATH,".//*[@style='height: 2.6em;' or @saria-hidden='true']")
driver.find_element(By.XPATH,".//*[text()='LG 1.5 Ton 5 Star AI DUAL Inverter Split…']").click()
#driver.find_element(By.XPATH,".//*[@class='nav-a  ' and @data-csa-c-slot-id='nav_cs_2']").click()
#driver.find_element(By.XPATH,".//*[@class='a-aui_72554-c a-aui_accordion_a11y_role_354025-c a-aui_killswitch_csa_logger_372963-c a-aui_launch_2021_ally_fixes_392482-t1 a-aui_pci_risk_banner_210084-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c a-aui_tnr_v2_180836-c a-meter-animate']").click()
#driver.find_element(By.XPATH,".//*[@href='/b?node=1389402031']").click()
#driver.find_element(By.XPATH,".//*[text()='Power banks']").click()
