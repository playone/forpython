# encoding: utf-8

from bs4 import BeautifulSoup
from selenium import webdriver
import time

counter = 0
browser = webdriver.Firefox()
browser.get('https://www.trivago.com.tw/?aDateRange%5Barr%5D=2017-10-25&aDateRange%5Bdep%5D=2017-10-28&aPriceRange%5Bto%5D=0&aPriceRange%5Bfrom%5D=0&iPathId=89626&aGeoCode%5Blng%5D=139.691711&aGeoCode%5Blat%5D=35.689487&iGeoDistanceItem=0&aCategoryRange=0%2C1%2C2%2C3%2C4%2C5&aOverallLiking=1%2C2%2C3%2C4%2C5&sOrderBy=relevance%20desc&bTopDealsOnly=false&iRoomType=7&cpt=8962603&iIncludeAll=0&iViewType=0&bIsSeoPage=false&bIsSitemap=false&')
time.sleep(4)
soup = BeautifulSoup(browser.page_source, 'html.parser')

while len(soup.select('.visuallyhidden')) > 0:
    for ele in soup.select('h3[class="name__copytext m-0 item__slideout-toggle"]'):
        print ele.text
        counter += 1
        ele.text
        with open('copy.txt', 'a') as f:
            f.write(ele.text.encode('utf-8') + '\n') #在此加上轉碼 可以確保寫入檔案不會發生encoding error
    browser.find_element_by_class_name('btn.btn--pagination.btn--small.btn--page-arrow.btn--next').click()
    time.sleep(4)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

browser.quit()
