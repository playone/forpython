# encoding: utf-8

import csv
from datetime import datetime
import urllib2
from bs4 import BeautifulSoup as bs

quote_page ='http://www.bloomberg.com/quote/SPX:IND'
page = urllib2.urlopen(quote_page)
soup = bs(page, 'html.parser')
print soup
name_box = soup.find('h1', attrs={'class' : 'name'})
name = name_box.text.strip()# strip() 函數用於去除前後空格
print name

price_box = soup.find('div', attrs={'class' : 'price'})
price = price_box.text.strip()
print price

with open('index.csv', 'a') as csv_file: #利用csv套件將資料存進csv 檔
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])