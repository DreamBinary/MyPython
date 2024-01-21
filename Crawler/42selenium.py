import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

path = "D:\MyPython\msedgedriver.exe"

browser = webdriver.Edge(executable_path=path)

# try:
#     browser.get("http://www.baidu.com")
#     input = browser.find_element_by_id("kw")
#     input.send_keys("Python")
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, "content_left")))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     print("-----------------")

browser.get("http://www.taobao.com")
input = browser.find_element_by_id('q')
input.send_keys("iphone")
time.sleep(1)
input.clear()
input.send_keys("ipad")
button = browser.find_element_by_class_name("btn_search")
button.click