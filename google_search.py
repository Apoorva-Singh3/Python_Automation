from selenium import webdriver
from selenium.webdriver.common.by import By




driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://amazon.com")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Shoes")
driver.find_element(By.ID, "nav-search-submit-button").click()

driver.close()