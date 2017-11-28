#encoding: utf-8

"""
抓取瀑布式網頁的範例
原本想抓取YAHOO新聞，但YAHOO block了 "window.scrollTo(0, document.body.scrollHeight);"這指令
所以假如想爬取YAHOO的資料得要使用另外的方法
"""

import xlwt
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

url_a = 'https://tw.eztable.com/channel/314'
driver = webdriver.Chrome()
driver.get(url_a)
time.sleep(2)


wb = xlwt.Workbook() #宣告excel檔案
sh= wb.add_sheet('A new sheet') #宣告新增一個新sheet
sh.write(0, 0, u'餐廳名稱') #新增某欄位內容 write(列, 欄, '欄位內容')
sh.write(0, 1, u'平均價位')
sh.write(0, 2, u'可預約時間')
sh.write(0, 3, u'餐廳網址')


def execute_times(times):
    for i in range(1, times+1):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #捲動頁面的語法 利用execute script 來執行 "window.scrollTo(0, document.body.scrollHeight);"這指令
        time.sleep(5)

execute_times(10) #呼叫函式 執行10次滾動頁面的動作

soup = bs(driver.page_source, 'html.parser')

# 選取我們要爬的資料定位元素 利用for loop 將在此bs dataframe裡面屬於這元素的文字爬出來, 並將爬取出來的文字寫入excel
h=0
for block in soup.select('h4.title'):
    h += 1
    sh.write( h, 0, block.text)
    print block.text

i=0
for block in soup.select('span.price-text'):
    i += 1
    sh.write(i, 1, block.text)
    print block.text

j=0
for block in soup.select('div.quota-wrapper'):
    j += 1
    sh.write(j, 2, block.text)
    print block.text

k=0
for block in soup.select('a'):
    url = str(block.get('href'))
    if '/restaurant/' in url:
        k += 1
        rest = 'https://tw.eztable.com'+url
        sh.write(k, 3, rest)
        print url


restlist = 'rest_list_'+time.strftime('%Y%m%d')+'.xls' #檔名會依日期生成
wb.save(restlist) #excel存檔
driver.quit()