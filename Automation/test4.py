# encoding: utf-8

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

def main():
    resp = requests.get('http://rate.bot.com.tw/xrt?Lang=zh-TW')
    soup = BeautifulSoup(resp.text, 'html.parser')

    rows = soup.find('table','table').tbody.find_all('tr')

    for row in rows:
        print [s for s in row.stripped_strings]


if __name__ == '__main__':
    main()