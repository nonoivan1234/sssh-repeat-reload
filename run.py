from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import time


def click(target):
    ActionChains(driver).move_to_element(target).perform()
    ActionChains(driver).click(target).perform()

print('run main.py')
url = 'https://www.sssh.tp.edu.tw/'

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
driver.get(url)

time.sleep(2)
i = 1

while True:
    print('progressing', i)
    btn = driver.find_element('xpath', '//a[@nid="21369"]')
    click(btn)
    close = driver.find_element('xpath', '//*[@id="layout"]/div[4]/a')
    click(close)
    print(i, 'complete')
    i += 1
