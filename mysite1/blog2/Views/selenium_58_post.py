from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
def publich_info(louceng):
    driver = webdriver.Chrome()
    driver.get('https://gz.58.com/house.shtml')
    driver.find_element_by_xpath('//*[@id="commonTopbar_login"]/a[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/img').click()
    username_input=driver.find_element_by_xpath('//*[@id="username"]')
    username_input.clear()
    username_input.send_keys('15818183032')
    pw_input=driver.find_element_by_xpath('//*[@id="password"]')
    pw_input.clear()
    pw_input.send_keys('a419832308')
    driver.find_element_by_xpath('//*[@id="btn_account"]').click()
    driver.implicitly_wait(200)


    driver.find_element_by_xpath('//*[@id="fabu"]').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[1]/a').click()
    time.sleep(2)

    input_xiaoqu  =driver.find_element_by_xpath('//*[@id="xiaoqu"]')

    input_xiaoqu.clear()
    input_xiaoqu.send_keys('横沙复建街住宅区')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="postForm"]/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li').click()

    time.sleep(2)

    input_si = driver.find_element_by_xpath('//*[@id="huxingshi"]')
    input_si.clear()
    input_si.send_keys('1')
    input_area = driver.find_element_by_xpath('//*[@id="area"]')
    input_area.clear()
    input_area.send_keys('30')
    input_float = driver.find_element_by_xpath('//*[@id="Floor"]')
    input_float.click()
    input_float.clear()
    input_float.send_keys('2')

    input_louceng = driver.find_element_by_xpath('//*[@id="zonglouceng"]')
    input_louceng.clear()
    input_louceng.send_keys('2')
    select_dianti = driver.find_element_by_xpath('//*[@id="postForm"]/div[1]/div[2]/div[4]/div[1]/div[4]/div[1]')
    select_dianti.click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="postForm"]/div[1]/div[2]/div[4]/div[1]/div[4]/div[2]/ul/li[2]').click()
    time.sleep(2)
    input_cost = driver.find_element_by_xpath('//*[@id="MinPrice"]')
    input_cost.clear()
    input_cost.send_keys('300')
    driver.find_element_by_xpath('//*[@id="postForm"]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="postForm"]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/ul/li[2]').click()
    time.sleep(2)
    upload_file = driver.find_element_by_xpath('//*[@id="imgUpload"]/div/input')
    upload_file.click()
    time.sleep(2)
    upload_file.send_keys(r'D:\1211test.jpg')
    input_owner = driver.find_element_by_xpath('//*[@id="goblianxiren"]')
    input_owner.clear()
    input_owner.send_keys('陈')
    driver.find_element_by_xpath('//*[@id="postForm"]/div[5]/div[2]/div[1]/div[1]/div[3]/div[2]').click()







