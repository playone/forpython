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

search_result = list(df.iloc[:, 1]) #宣告變數，將dataframework的第二欄轉成List, 下面會將搜尋完成的結果放到這裡
#print df
def search_keyword(word): #word 在接下來的引用，會從excel那邊得到值來做此方法的動作
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys(word)
    driver.find_element_by_id('su').click()
    #利用webdriver, 將頁面帶到要處理的地方
    time.sleep(3)
    result = driver.find_element_by_xpath('//*[@id="2"]/h3/a[1]')
    return result.text #定義函式, 搜尋關鍵字並將文字結果回傳出來

for index, word in enumerate(list(df.iloc[:, 0])):
    '''
    先用list將excel裡面的第一欄位的關鍵字列出來，再用enumerate 組成索引序列
    index對應的就是索引序列的index, word則是索引序列裡面的值
    '''
    search_result[index] = search_keyword(word) #呼叫函式運行, 利用word做關鍵字搜尋，再將結果回放到search_result
    #print search_result

df.iloc[:, 1] = search_result #回存到pandas 的dataframework

df.to_excel('search_result.xls', index = False) #存檔。 index=faulse 表示不需寫入index到excel

driver.quit()
