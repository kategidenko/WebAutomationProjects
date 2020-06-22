import time
from selenium import webdriver

driver = webdriver.Chrome('C:\chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.ebay.com/')
searchbox = driver.find_element_by_id("gh-ac")
searchbox.send_keys('potato')
searchbox.submit()

time.sleep(2)
driver.quit()