from selenium import webdriver
import time

site1 = "https://youtube.com"
site2 = "https://twitter.com"
site3 = "https://instagram.com"

 
driver = webdriver.Chrome(executable_path="C:/Users/a/apoorva/basicPythonAutomation/drivers/chromedriver.exe")

driver.implicitly_wait(10)
driver.maximize_window()
driver.get(site1)
driver.execute_script("window.open('about:blank','second tab');")
driver.switch_to.window("second tab")
driver.get(site2)
time.sleep(1)
driver.execute_script("window.open('about:blank','third tab');")
driver.switch_to.window("third tab")
driver.get(site3)
time.sleep(5)

driver.quit()