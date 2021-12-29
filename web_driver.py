from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()
driver.maximize_window()

# Login to Twitter
driver.get("https://twitter.com/login?lang=en-gb")
time.sleep(3)
driver.find_element_by_name('text').send_keys('usename')
time.sleep(3)
# driver.find_element_by_xpath(
#     '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span').click()
driver.find_element_by_xpath(
    '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span').click()
time.sleep(3)
# driver.find_element_by_xpath("//span[text()='Next']").click()


driver.find_element_by_name('text').send_keys('Email')
time.sleep(3)
driver.find_element_by_xpath(
    '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div').click()
time.sleep(3)

driver.find_element_by_name('password').send_keys('Password')
time.sleep(3)
driver.find_element_by_xpath(
    '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/span').click()
time.sleep(3)

# Tweet
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div').send_keys('Hello Its Twitter Bot')
time.sleep(3)

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(3)

# Click Explore Button
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div/div[2]').click()
time.sleep(3)

# Click Search Input Field
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input').send_keys('@Cristiano')
time.sleep(3)

driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div[4]/div/div/div/div[2]').click()
time.sleep(3)

# Follow someone
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/span/span').click()
time.sleep(3)


# Log out
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[1]').click()
time.sleep(3)
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]/div').click()
time.sleep(3)
# Confirm Button
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span').click()
time.sleep(3)

print('TEst Completed')

driver.close()
