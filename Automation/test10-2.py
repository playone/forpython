# encoding: utf-8

"""
爬蟲爬POST的練習 強化版
有利用過urllib+bs 抓取跟分析網頁
後來換成 requests+pandas抓取表格
"""


import requests
import pandas
from bs4 import BeautifulSoup as bs
import urllib,urllib2

url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
request = urllib2.Request(url)
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") #設定好header避免被判別為機器人

startstation_name = int(raw_input('請輸入數字代表開始的站名: 1.南港 2.台北 3.板橋 4.桃園 5.新竹 6.苗栗 7.台中 8.彰化 9.雲林 10.嘉義 11.台南 12.左營' + '\n'))
endstation_name = int(raw_input('請輸入數字代表終點站名: 1.南港 2.台北 3.板橋 4.桃園 5.新竹 6.苗栗 7.台中 8.彰化 9.雲林 10.嘉義 11.台南 12.左營' + '\n'))
search_data = str(raw_input('請輸入日期: (例如 2017/01/01) ' + '\n'))
search_time = str(raw_input('請輸入時間: (例如 12:30, 請以半小時為區隔)' + '\n'))
#使用者輸入想要查詢的資料，台鐵網頁會用post來傳輸資料

stations = [ #各站名在高鐵網頁post裡面的form data 代碼，在這裡存成串列，之後直接呼叫帶入 formdata
    '2f940836-cedc-41ef-8e28-c2336ac8fe68', #南港
    '977abb69-413a-4ccf-a109-0272c24fd490', #台北
    'e6e26e66-7dc1-458f-b2f3-71ce65fdc95f', #板橋
    'fbd828d8-b1da-4b06-a3bd-680cdca4d2cd', #桃園
    'a7a04c89-900b-4798-95a3-c01c455622f4', #新竹
    'e8fc2123-2aaf-46ff-ad79-51d4002a1ef3', #苗栗
    '3301e395-46b8-47aa-aa37-139e15708779', #台中
    '38b8c40b-aef0-4d66-b257-da96ec51620e', #彰化
    '5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f', #雲林
    '60831846-f0e4-47f6-9b5b-46323ebdcef7', #嘉義
    '9c5ac6ca-ec89-48f8-aab0-41b738cb1814', #台南
    'f2519629-5973-4d08-913b-479cce78a356'  #左營
]

form_data = {
    "StartStation": stations[startstation_name-1], #帶入使用者輸入的起點站
    "EndStation": stations[endstation_name-1],     #帶入使用者輸入的終點站
    "SearchDate": search_data,                     #帶入使用者輸入的日期
    "SearchTime": search_time,                     #帶入使用者輸入的時間
    "SearchWay":"DepartureInMandarin",
    "RestTime":"",
    "EarlyOrLater":""
}

res = requests.post("http://www.thsrc.com.tw/tw/TimeTable/SearchResult", data=form_data) #利用request.post帶出搜尋結果網頁

info = pandas.read_html(res.text, header=0)[0] #用pandas存成data frame 然後提取table出來
info = info.ix[1:, 1:5]
info.columns = [u'車次', u'出發時間', u'抵達時間', u'行車時間']
info = info.dropna()
print info #列印結果

info.to_excel('traintime.xlsx', encoding='UTF-8', index=False) #轉入excel


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




