# encoding: utf-8

"""
爬蟲爬POST的練習 強化版
"""

import urllib,urllib2
import requests
import pandas
from bs4 import BeautifulSoup as bs


url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
request = urllib2.Request(url)
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

startstation_name = int(raw_input('請輸入數字代表開始的站名: 1.南港 2.台北 3.板橋 4.桃園 5.新竹 6.苗栗 7.台中 8.彰化 9.雲林 10.嘉義 11.台南 12.左營' + '\n'))
endstation_name = int(raw_input('請輸入數字代表終點站名: 1.南港 2.台北 3.板橋 4.桃園 5.新竹 6.苗栗 7.台中 8.彰化 9.雲林 10.嘉義 11.台南 12.左營' + '\n'))
search_data = str(raw_input('請輸入日期: (例如 2017/01/01) ' + '\n'))
search_time = str(raw_input('請輸入時間: (例如 12:30, 請以半小時為區隔)' + '\n'))


stations = [
    '2f940836-cedc-41ef-8e28-c2336ac8fe68',
    '977abb69-413a-4ccf-a109-0272c24fd490',
    'e6e26e66-7dc1-458f-b2f3-71ce65fdc95f',
    'fbd828d8-b1da-4b06-a3bd-680cdca4d2cd',
    'a7a04c89-900b-4798-95a3-c01c455622f4',
    'e8fc2123-2aaf-46ff-ad79-51d4002a1ef3',
    '3301e395-46b8-47aa-aa37-139e15708779',
    '38b8c40b-aef0-4d66-b257-da96ec51620e',
    '5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f',
    '60831846-f0e4-47f6-9b5b-46323ebdcef7',
    '9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
    'f2519629-5973-4d08-913b-479cce78a356'
]

form_data = {
    "StartStation": stations[startstation_name-1],
    "EndStation": stations[endstation_name-1],
    "SearchDate": search_data,
    "SearchTime": search_time,
    "SearchWay":"DepartureInMandarin",
    "RestTime":"",
    "EarlyOrLater":""
}

res = requests.post("http://www.thsrc.com.tw/tw/TimeTable/SearchResult", data=form_data)

info = pandas.read_html(res.text, header=0)[0]
print info

info.to_excel('traintime.xlsx', encoding='UTF-8', index=False)


"""
form_data = urllib.urlencode(form_data)
response = urllib2.urlopen(request, data=form_data)
html = response.read()

print type(html)

soup = bs(html, 'html.parser')

table = soup.select('section.result_table')


file_out = file("table.txt",'w')
file_out.write(str(table).encode('utf-8'))
file_out.close()
"""




