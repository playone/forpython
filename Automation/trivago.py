# encoding: utf-8

from bs4 import BeautifulSoup
from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://www.trivago.com.tw/?aDateRange%5Barr%5D=2017-10-15&aDateRange%5Bdep%5D=2017-10-19&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iPathId=89626&aGeoCode%5Blat%5D=35.689487&aGeoCode%5Blon%5D=139.691711&iGeoDistanceItem=0&aCategoryRange=0%2C1%2C2%2C3%2C4%2C5&aOverallLiking=1%2C2%2C3%2C4%2C5&sOrderBy=relevance%20desc&bTopDealsOnly=false&iRoomType=7&cpt=8962603&iIncludeAll=0&iViewType=0&bIsSeoPage=false&bIsSitemap=false&')

soup = BeautifulSoup(browser.page_source, 'html.parser')
while len(soup.select('.visuallyhidden')) > 0:
    for ele in soup.select('h3[class="name__copytext m-0 item__slideout-toggle"]'):
        print ele.text
        with open('copy.txt', 'a') as f:
           f.write(ele.text+ '\n')
    browser.find_element_by_css_selector('.btn--page-arrow').click()
    soup = BeautifulSoup(browser.page_source, 'html.parser')
browser.quit()
