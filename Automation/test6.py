# encoding: utf-8

"""
利用excel讀入關鍵字做搜尋
百度的網頁程式碼結構比google更容易去閱讀
因此拿它來來做練習的目標
"""

import pandas as pd
import time
from selenium import webdriver


df = pd.read_excel('keywords.xls') #將excel 內容轉存成dataframework
#print df
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

search_result = list(df.iloc[:, 1]) #將dataframework的第二欄放到search_result, 下面會將搜尋完成的結果放到這裡

def search_keyword(word):
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys(word)
    driver.find_element_by_id('su').click()

    time.sleep(3)
    result = driver.find_element_by_xpath('//*[@id="2"]/h3/a[1]')
    return result.text #定義函式, 搜尋關鍵字並將文字結果回傳出來

for index, word in enumerate(list(df.iloc[:, 0])): #此for loop, index對應到 df.iloc的列, word對應到欄
    search_result[index] = search_keyword(word) #呼叫函式運行, 並將結果回傳給list的第二欄
    #print search_result

df.iloc[:, 1] = search_result #list存成dataframework

df.to_excel('search_result.xls', index = False) #存檔

driver.quit()