#unicode: utf-8

"""
抓取瀑布式網頁的範例
"""


from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

url = 'https://tw.eztable.com/channel/314'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

def execute_times(times):
    for i in range(1, times+1):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #捲動頁面的語法 利用execute script 來執行 "window.scrollTo(0, document.body.scrollHeight);"這指令
        time.sleep(5)

execute_times(10) #呼叫函式 執行10次滾動頁面的動作

soup = bs(driver.page_source, 'html.parser')

for block in soup.select('h4.title'): #選取我們要爬的資料定位元素 利用for loop 將頁面裡面屬於這元素的文字爬出來
    print block.text

driver.quit()