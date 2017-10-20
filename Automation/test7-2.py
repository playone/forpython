#encoding: utf-8

"""
test7的加強版
爬取多個網頁的資料
"""

import urllib2
from bs4 import BeautifulSoup as bs
import csv
from datetime import datetime

quote_page = [
    'http://www.bloomberg.com/quote/SPX:IND',
    'http://www.bloomberg.com/quote/CCMP:IND'
]
data = []

for pg in quote_page:
    page = urllib2.urlopen(pg)
    soup = bs(page, 'html.parser')
    namebox = soup.find('h1', attrs={'class': 'name'})
    name = namebox.text.strip()
    pricebox = soup.find('div', attrs={'class': 'price'})
    price = pricebox.text.strip()
    data.append((name, price)) # 把提取出來的name和price 放到data
    with open('index2.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        for name, price in data: # 用for loop把data裡面的資料寫入csv
            writer.writerow([name, price, datetime.now()])