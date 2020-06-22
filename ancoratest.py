# test the service page 

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('C:\chromedriver')
#actions = ActionChains(driver)


driver.get('https://www.ancoracenter.com/')

readmore = driver.find_element_by_link_text('Read more...')
readmore.click()

time.sleep(2)
terms = driver.find_element_by_css_selector('.terms')
terms.click()

time.sleep(2)

accept = driver.find_element_by_xpath('//span[text() = " I accept "]')

accept.click()

services = driver.find_element_by_xpath('//span[text()= "Services"]')
services.click()

forms = driver.find_element_by_xpath('//span[text()= "Forms"]')
forms.click()

time.sleep(2)


forms_yelena = intake = driver.find_elements_by_xpath('//h2[text() = "Forms"]/../div/div/table/tbody/tr/td[2]/a')
forms_quintisha = intake = driver.find_elements_by_xpath('//h2[text() = "Forms"]/../div/div/table/tbody/tr/td[3]/a')

for form in forms_yelena:
    action = ActionChains(driver)
    action.move_to_element(form)
    action.perform()
    form.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

for form in forms_quintisha:
    action = ActionChains(driver)
    action.move_to_element(form)
    action.perform()
    form.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

resources = driver.find_element_by_xpath('//span[text()= "Resources"]')
resources.click()

titles = driver.find_elements_by_xpath('//h2[text() = "Resources"]/../div/div/div[1]')
title_labels = []
for i in titles:
    title_labels.append(i.text)

print(title_labels)

contact = driver.find_element_by_xpath('//span[text()="Contact"]')
contact.click()

info = driver.find_element_by_xpath('//h2[text() = "Contact Us"]/../div/div/div/div/div')
print(info.text)


time.sleep(5)

driver.quit()
