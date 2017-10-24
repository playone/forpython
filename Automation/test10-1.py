# encoding: utf-8

"""
爬蟲爬POST的練習
"""

import urllib,urllib2
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
request = urllib2.Request(url)
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")



form_data = {
    "StartStation": "2f940836-cedc-41ef-8e28-c2336ac8fe68",
    "EndStation": "5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f",
    "SearchDate": "2017/10/24",
    "SearchTime": "15:30",
    "SearchWay":"DepartureInMandarin",
    "RestTime":"",
    "EarlyOrLater":""
}
form_data = urllib.urlencode(form_data)
response = urllib2.urlopen(request,data=form_data)
html = response.read()
print type(html)
file_out = file("test.html",'w')
file_out.write(html)
file_out.close()