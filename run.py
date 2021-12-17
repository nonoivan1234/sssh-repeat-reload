from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

url = 'https://www.sssh.tp.edu.tw/ischool/widget/site_news/news_pop_content.php?newsId=21369&maxRows_rsResult=5&fh=0&bid=0&uid=WID_0_2_09f98f0ccd62cf30e882f06ffe93ca89d6a81b39'



# def click(target):
    # ActionChains(driver).move_to_element(target).perform()
    # ActionChains(driver).click(target).perform()

# url = 'https://www.sssh.tp.edu.tw/'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

time.sleep(3)
i = 1

while(True):
  driver.refresh()
  print('completing', i)
  i+=1
# while True:
#     try:
#         print('progressing', i)
#         btn = driver.find_element('xpath', '//a[@nid="21369"]')
#         # print('driver find btn', i)
#         click(btn)
#         print(i, 'complete')
#         close = driver.find_element('xpath', '//*[@id="layout"]/div[4]/a')
#         # print('driver find close', i)
#         click(close)
#         i += 1
#     except:
#         print('FAILED click close', i)
#         i += 1
#         driver.get(url)
#         time.sleep(3)
