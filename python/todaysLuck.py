import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome('/home/user/다운로드/chromedriver')

driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8')

time.sleep(3)

birthday = driver.find_element_by_xpath('//*[@id="srch_txt"]')

birthday.send_keys('20000519')

search = driver.find_element_by_xpath('//*[@id="fortune_birthCondition"]/div[1]/fieldset/input')
search.click()

time.sleep(3)

