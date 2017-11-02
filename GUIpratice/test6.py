#encoding: utf-8

"""
GUI實際練習
將Automation\test10-2 GUI化
"""


from Tkinter import *
import requests
import urllib2
import pandas



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

url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
request = urllib2.Request(url)
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") #設定好header避免被判別為機器人


def okbutton_click():
    startstation_name = int(entryStartStation.get())
    endstation_name = int(entryEndStation.get())
    search_data = str(entryDate.get())
    search_time = str(entryTime.get())
    form_data = {
        "StartStation": stations[startstation_name - 1],  # 帶入使用者輸入的起點站
        "EndStation": stations[endstation_name - 1],  # 帶入使用者輸入的終點站
        "SearchDate": search_data,  # 帶入使用者輸入的日期
        "SearchTime": search_time,  # 帶入使用者輸入的時間
        "SearchWay": "DepartureInMandarin",
        "RestTime": "",
        "EarlyOrLater": ""
    }
    res = requests.post("http://www.thsrc.com.tw/tw/TimeTable/SearchResult", data=form_data)  # 利用request.post帶出搜尋結果網頁

    info = pandas.read_html(res.text, header=0)[0]  # 用pandas存成data frame 然後提取table出來
    print info  # 列印結果
    text.insert(1.0, info)
    #labelResult.configure(text = info)

root = Tk()
title = root.title('高鐵時刻查詢')

labelStartStation = Label(root, text = '請輸入數字代表開始的站名: 1.南港 2.台北 3.板橋 4.桃園 5.新竹 6.苗栗 7.台中 8.彰化 9.雲林 10.嘉義 11.台南 12.左營').pack(fill = X)
entryStartStation = Entry(root)
entryStartStation.pack(fill = X)
labelEndStation = Label(root, text = '請輸入數字代表終點站名: 1.南港 2.台北 3.板橋 4.桃園 5.新竹 6.苗栗 7.台中 8.彰化 9.雲林 10.嘉義 11.台南 12.左營').pack(fill = X)
entryEndStation = Entry(root)
entryEndStation.pack(fill = X)
labelDate = Label(root, text = '請輸入日期: (例如 2017/01/01)').pack(fill = X)
entryDate = Entry(root)
entryDate.pack(fill = X)
labelTime = Label(root, text = '請輸入時間: (例如 12:30, 請以半小時為區隔)').pack(fill = X)
entryTime = Entry(root)
entryTime.pack(fill = X)

buttonok = Button(root, text = 'OK', command = okbutton_click).pack(fill = Y)
buttoncancel = Button(root, text = 'Close', command = root.quit).pack(fill = Y)

labelResult = Label(root, text = '結果').pack(fill = X)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, wrap=WORD, yscrollcommand=scrollbar.set)
text.pack()

scrollbar.config(command=text.yview)

root.mainloop()