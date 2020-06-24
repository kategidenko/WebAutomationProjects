import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('C:\chromedriver')
driver.get('https://www.ancoracenter.com/')

readmore = driver.find_element_by_link_text('Read more...')
readmore.click()

time.sleep(2)
terms = driver.find_element_by_css_selector('.terms')
terms.click()

time.sleep(2)

accept = driver.find_element_by_xpath('//span[text() = " I accept "]')
action = ActionChains(driver)
action.move_to_element(accept)
action.perform()
accept.click()


services = driver.find_element_by_xpath('//span[text()= "Services"]')
services.click()

time.sleep(2)
more_services = driver.find_element_by_xpath('//span[text()= " More Services... "]')
action = ActionChains(driver)
action.move_to_element(more_services)
action.perform()
more_services.click()

pay_now = driver.find_elements_by_xpath('//span[text() = "Pay Now"]')

pay_now[0].click()
time.sleep(2)
therapist = driver.find_element_by_xpath('//label[text()="Therapist*"]/../div')
therapist.click()
time.sleep(2)
yelena = driver.find_element_by_xpath('//div[text()="Dr. Yelena Gidenko"]')
yelena.click()

initials = driver.find_element_by_id("input-160")
initials.send_keys('kg')

calender = driver.find_element_by_id("input-164")
calender.click()

time.sleep(2)

date = driver.find_element_by_xpath('//div[contains(@class, "v-picker--date")]/*//div[text() = "14"]')
date.click()

time.sleep(2)
amount = driver.find_element_by_xpath('//label[text() = "Amount*"]/../input')
amount_1 = amount.get_attribute('value')
print("One 60 min session with Yelena: ", amount_1)


therapist = driver.find_element_by_xpath('//label[text()="Therapist*"]/../div')
therapist.click()
time.sleep(2)
quintisha = driver.find_element_by_xpath('//div[text()="Quintisha China, LCSW"]')
quintisha.click()

time.sleep(2)
amount = driver.find_element_by_xpath('//label[text() = "Amount*"]/../input')
amount_1 = amount.get_attribute('value')
print("One 60 min session with Quintisha: ", amount_1)

time.sleep(2)

leave_page = driver.find_element_by_xpath('//span[text() = "Make a Payment"]/../../div[3]')
leave_page.click()

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
