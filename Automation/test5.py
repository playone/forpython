# encoding: utf-8

import  pandas #導入pandas

dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
"""
pandas 導入網頁資料之後, 會將網頁資料存成list > data framework
因此我們下一步就是將這data framework提取出來
"""
currency = dfs[0] #提取data framework

currency = currency.ix[:, 0:5] #提取某固定欄位 [列, 欄], : 是全提取, 0:5 是指提取1~5欄
currency.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行買出', u'即期匯率-本行買入', u'即期匯率-本行買出']
#更換欄位名稱轉存到excel, u 是指將名稱換成unicode
currency[u'幣別'] = currency[u'幣別'].str.extract(r'\((\w+)\)', expand = True) #提取欄位某名稱
currency.to_excel('currency.xlsx') #存到excel檔案