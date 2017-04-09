# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *

try:
    driver = webdriver.Ie()
    driver.get("http://www.baidu.com")

    driver.find_element_by_xpath("//input[@id='kw']").send_keys("robot framework")
    sleep(2)
    driver.find_element_by_xpath("//input[@id='su']").click()
    sleep(5)
except BaseException as msg:
    print(msg)
finally:
    driver.quit()


sleep(2)
try:
    driver = webdriver.Ie()
    driver.get("http://www.baidu.com")

    driver.find_element(By.XPATH,"//input[@id='kw']").send_keys("robot framework")
    sleep(2)
    driver.find_element(By.ID,'su').click()
    sleep(5)
except BaseException as msg:
    print(msg)
finally:
    driver.quit()
