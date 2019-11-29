from django.test import TestCase
import requests,json,time
# Create your tests here.
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://gz.58.com/")
join_login_page = driver.find_element_by_xpath("//*[@id='commonTopbar_login']/a[1]")
join_login_page.click()
driver.implicitly_wait(20)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/span').click()
input_user = driver.find_element_by_xpath("//*[@id='username']")
input_user.clear()
input_user.send_keys("15818183032")
input_pw = driver.find_element_by_xpath("//*[@id='password']")
input_pw.clear()
input_pw.send_keys("a419832308")
driver.find_element_by_xpath("//*[@id='btn_account']").click()
driver.implicitly_wait(20)
cookie = driver.get_cookies()
j_cookie = json.dumps(cookie)

with open("58_cookie.json","w")as f:
    try:
        f.write(str(j_cookie))
    except Exception as e:
        print(e)
f.close()

driver.close()


# driver2 = webdriver.Chrome()
# driver2.get("https://gz.58.com/")



