from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from lxml import etree
import random

IPPOOL = [
        {'ipaddr': 'http://222.173.215.170:8080'},
        {'ipaddr': 'http://39.137.46.77:80'},
        {'ipaddr': 'http://120.25.203.182:7777'},
        {'ipaddr': 'http://117.191.11.79:80'},
    ]


proxy = random.sample(IPPOOL, 1)[0]['ipaddr']
print(proxy)

driver_path = 'D:\DGQsoft\chromedriver_win32\chromedriver.exe'
options =webdriver.ChromeOptions()
options.add_argument("--proxy-server="+proxy)
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
# driver_cm = webdriver.Chrome(executable_path=driver_path)

driver.get('http://www.dianping.com/shop/502331')