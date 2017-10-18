# encoding: utf-8

"""
簡單的python呼叫selenium程式
"""

from selenium import webdriver #呼叫webdriver
from selenium.webdriver.common.keys import Keys #模擬輸入的函式

driver = webdriver.Firefox() #定義以FIREFOX為主的webdriver
driver.get('http://www.python.org') #開啟網頁
assert 'Python' in driver.title #判定網頁title裡面有含某個關鍵字
elem = driver.find_element_by_name('q') #將被定位的元素所關聯的內容定義出來
elem.clear() # elem此元素是一個輸入欄位, 此class是將欄位內容清空
elem.send_keys('pycon') #輸入文字
elem.send_keys(Keys.RETURN) #模擬按鍵
assert 'No results found' not in driver.page_source
driver.get_screenshot_as_file('screenshot/test.png') #截圖
driver.quit() #關閉webdriver釋放空間