#encoding: utf-8

"""
輸入數字當作爬取的頁數的練習
現在這檔案有轉碼的問題
"""

import requests
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')

page = int(input("請輸入要擷取的頁數"))
for i in range(1,page+1):
    res = requests.get("https://www.mobile01.com/forumtopic.php?c=17&p="+ str(i))
    soup = BeautifulSoup(res.text,"html.parser")
    for title in soup.select(".topic_gen"):
        print ("==============")
        url = str(title.get('href'))
        result = ("[標題]:"+title.text, "\n"+"https://www.mobile01.com/"+url)
        print result
        with open('copy1.txt', 'a') as f:
            f.write(str(result) + '\n')
