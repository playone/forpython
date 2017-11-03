#encoding: utf-8

"""
GUI實際練習
將Automation\test10-2 GUI化 part2
使用到的widget: button, optionmenu, calendar
"""

from ttkcalendar import *
from Tkinter import *
import requests
import urllib2
import pandas


stations = { #各站名在高鐵網頁post裡面的form data 代碼，在這裡存成字典，之後直接呼叫帶入 formdata
    u'南港':'2f940836-cedc-41ef-8e28-c2336ac8fe68', #南港
    u'台北':'977abb69-413a-4ccf-a109-0272c24fd490', #台北
    u'板橋':'e6e26e66-7dc1-458f-b2f3-71ce65fdc95f', #板橋
    u'桃園':'fbd828d8-b1da-4b06-a3bd-680cdca4d2cd', #桃園
    u'新竹':'a7a04c89-900b-4798-95a3-c01c455622f4', #新竹
    u'苗栗':'e8fc2123-2aaf-46ff-ad79-51d4002a1ef3', #苗栗
    u'台中':'3301e395-46b8-47aa-aa37-139e15708779', #台中
    u'彰化':'38b8c40b-aef0-4d66-b257-da96ec51620e', #彰化
    u'雲林':'5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f', #雲林
    u'嘉義':'60831846-f0e4-47f6-9b5b-46323ebdcef7', #嘉義
    u'台南':'9c5ac6ca-ec89-48f8-aab0-41b738cb1814', #台南
    u'左營':'f2519629-5973-4d08-913b-479cce78a356'  #左營
}

dropdown_options_stations = [
    '南港',
    '台北',
    '板橋',
    '桃園',
    '新竹',
    '苗栗',
    '台中',
    '彰化',
    '雲林',
    '嘉義',
    '台南',
    '左營'
]

dropdown_options_time = [
    '05:00',
    '05:30',
    '06:00',
    '06:30',
    '07:00',
    '07:30',
    '08:00',
    '08:30',
    '09:00',
    '09:30',
    '10:00',
    '10:30',
    '11:00',
    '11:30',
    '12:00',
    '12:30',
    '13:00',
    '14:00',
    '14:30',
    '15:00',
    '15:30',
    '16:00',
    '16:30',
    '17:00',
    '17:30',
    '18:00',
    '18:30',
    '19:00',
    '19:30',
    '20:00',
    '20:30',
    '21:00',
    '21:30',
    '22:00',
    '22:30',
    '23:00',
    '23:30',
    '24:00'
]

url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
request = urllib2.Request(url)
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") #設定好header避免被判別為機器人


def okbutton_click():
    result = calendar.selection
    startstation_code = stations[variable_startstation.get()]
    endstation_code = stations[variable_endstation.get()]
    search_data = str(result)[0:10].replace('-', '/')
    print search_data
    search_time = variable_time.get() #str(entryTime.get())
    form_data = {
        "StartStation": startstation_code,  # 帶入使用者輸入的起點站
        "EndStation": endstation_code,  # 帶入使用者輸入的終點站
        "SearchDate": search_data,  # 帶入使用者輸入的日期
        "SearchTime": search_time,  # 帶入使用者輸入的時間
        "SearchWay": "DepartureInMandarin",
        "RestTime": "",
        "EarlyOrLater": ""
    }
    res = requests.post("http://www.thsrc.com.tw/tw/TimeTable/SearchResult", data=form_data)  # 利用request.post帶出搜尋結果網頁

    info = pandas.read_html(res.text, header=0)[0]  # 用pandas存成data frame 然後提取table出來
    info = info.ix[1:, 1:5]
    info.columns = [u'車次', u'出發時間', u'抵達時間', u'行車時間']
    info = info.dropna()
    print info  # 列印結果
    text.insert(1.0, info)
    #labelResult.configure(text = info)

root = Tk()
title = root.title('高鐵時刻查詢')

variable_startstation = StringVar(root)
variable_startstation.set(dropdown_options_stations[0])
variable_endstation = StringVar(root)
variable_endstation.set(dropdown_options_stations[11])
variable_time = StringVar(root)
variable_time.set(dropdown_options_time[0])

labelStartStation = Label(root, text = '請選擇開始的站名:').pack(fill = X)
optionStartStation = OptionMenu(root, variable_startstation, *dropdown_options_stations)
optionStartStation.pack(fill=X)

labelEndStation = Label(root, text = '請選擇終點的站名:').pack(fill = X)
optionEndStation = OptionMenu(root, variable_endstation, *dropdown_options_stations)
optionEndStation.pack(fill=X)

labelDate = Label(root, text = '請選擇日期:').pack(fill = X)
calendar = Calendar(root)
calendar.pack()


labelTime = Label(root, text = '請選擇時間:').pack(fill = X)
optionTime = OptionMenu(root, variable_time, *dropdown_options_time)
optionTime.pack(fill=X)

buttonok = Button(root, text = 'OK', command = okbutton_click).pack(fill = Y)
buttoncancel = Button(root, text = 'Close', command = root.quit).pack(fill = Y)

labelResult = Label(root, text = '結果').pack(fill = X)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, wrap=WORD, yscrollcommand=scrollbar.set)
text.pack()

scrollbar.config(command=text.yview)

root.mainloop()