# encoding: utf-8

import requests
import lxml.html
import sys
import json
import pandas as pd
import time

reload(sys)
sys.setdefaultencoding('utf8')
df = pd.read_excel('copy.xls')
url = 'http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml'
html = requests.get(url).text
doc = lxml.html.fromstring(html)

search_title = list(df.iloc[:, 0])
search_link = list(df.iloc[:, 1])

titles = doc.xpath('//div[@class="newsList"]/ul/li/a/text()')
href = doc.xpath('//div[@class="newsList"]/ul/li/a/@href')
i=0
j=0
for i in len(titles):
    df.iloc[:, 0] = titles[i]

for j in len(href):
    df.iloc[:, 1] = href[j]

df.to_excel('copy.xls', index = False)

"""
i = 0
for content in titles:
    results = {'標題': titles[i], '鏈結': href[i]}
    i += 1
    print results
    jsonobj = json.dumps(results)
    fileobj = open('jsonfile.json', 'a')
    fileobj.write(jsonobj)
    fileobj.close()
"""