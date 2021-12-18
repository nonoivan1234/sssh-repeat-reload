from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


url = 'https://www.sssh.tp.edu.tw/ischool/widget/site_news/news_pop_content.php?newsId=21369&maxRows_rsResult=5&fh=0&bid=0&uid=WID_0_2_09f98f0ccd62cf30e882f06ffe93ca89d6a81b39'

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
