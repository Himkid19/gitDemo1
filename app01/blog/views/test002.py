
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
select_edit = driver.find_element_by_xpath('//*[@id="kw"]')
select_edit.clear()
select_edit.send_keys('python')
ActionChains(driver).move_to_element(select_edit).perform()
driver.find_element_by_xpath('//*[@id="form"]/div/ul/li[1]').click()


driver.close()