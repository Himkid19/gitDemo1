from selenium import webdriver
import json,time

driver = webdriver.Chrome()
driver.get("https://gz.58.com/")
driver.delete_all_cookies()
f = open("58_cookie.json")
cookie = f.read()
f.close()
cookie = json.loads(cookie)

for i in cookie:
    if 'expiry' in i:
        del cookie['expiry']
    driver.add_cookie(i)
driver.refresh()
driver.implicitly_wait(20)
time.sleep(5)
driver.close()
