#! python2.7
#encoding: utf-8

"""
此程式的功能是用來提醒redmine 使用者issue 超過三天或者超過due day 還未更新。
當判別有此情況發生時，會寄信給使用者作提醒。
自行程式客製化完成之後，可放於OS的排程裡面定期執行。
Gmail 的SMTP server假如有遇到無法連線狀態，可以到以下的網址參考做設定
https://jamching.com/article/Python-to-Send-Email-1.html
"""

import smtplib
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from datetime import date


server_url = 'http://172.16.1.25' #Remine Server的 IP/Domain address
query_url = 'http://172.16.1.25/projects/internal/issues?query_id=17' #Redmine issue query 的 IP/Domain Address
cookies = {'_redmine_session':' '}
#Remine 登入的cookie, 自行換成其他帳號的登入資訊, 只是要小心外流

# 輸入gmail信箱的資訊
host = "smtp.gmail.com" #Gmail的SMTP address
port = 587              #Gmail的SMTP port
username = "account@gmail.com" #Gmail登入帳號
password = "password"         #Gmail登入密碼
from_email = username          #程式送信人會使用的email 帳號，在這裡設定成跟Gmail登入帳號一樣
to_list = ['safe.yang@iisigroup.com'] #一開始預設的收信人的email帳號，在這我會定義成一個可供測試的email帳號做測試收信用


def setup(url, cookies):
    """
    此函試是每個函式必做的步驟，將query頁面的table提取出來，存成dateframe，同時新增兩個欄位Over 3 Day, Over Due Day
    :param url: issue query url
    :param cookies: redmine cookies
    :return: query table's dataframe
    """
    res = requests.get(url, cookies=cookies)
    soup = bs(res.content, 'html.parser')
    table = soup.find_all('table')
    df = pd.read_html(str(table))
    table2 = df[2] #在query 頁面裡應該會找到3個table, 而第3個table是我們所需要的table
    table2 = table2.ix[:, 1:] #選取所需的table column
    table2.columns = ['Issue ID', 'Tracker', 'Status', 'Priority', 'Subject', 'Assignee', 'Updated', 'Created', 'Due date']
    #重新命名欄位名稱
    table2['Over 3 Day'] = None #新增column "Over 3 Day"。假如issue 超過3天沒更新，會在這欄位寫入值"True"。反之則填入值"False"
    table2['Over Due Day'] = None #新增column "Over Due Day"。假如issue 超過Due Day沒更新，會在這欄位寫入值"True"。反之則填入值"False"
    return table2

def get_mail(issue_id, assignee, cookies):
    """
    從issue info 頁面導到user info 頁面擷取user 的email address，以供寄信流程作業
    :param issue_id: issue id
    :param assignee: issue assignnee
    :param cookies: redmine cookies
    :return: issue assignee email address
    """
    url = server_url+'/issues/'+str(issue_id) #issue info address
    res = requests.get(url, cookies=cookies)
    soup = bs(res.text, 'html.parser')

    for block in soup.select('[class="user active"]'):
        """
        擷取assignee 的user info address
        """
        if assignee in block.text:
            user = block.get('href')

    url2 = server_url+user #user info address
    res2 = requests.get(url2)
    soup2 = bs(res2.text, 'html.parser')

    mailcheck = 0
    for block2 in soup2.find_all('a'):
        """
        擷取assignee 的email.
        mailcheck是用來判別是否有抓取到email。
        假如沒抓取到email，會自動給一個email address "nomail@nomail"。
        以利於admin判別並要求使用者更新email
        """
        if '@' in block2.text:
            mail = block2.text
            mailcheck = 1

    if mailcheck == 0:
        mail = 'nomail@nomail'

    return str(mail)


def over_due_day(url = query_url, cookies = cookies):
    """
    以due day為基準，假如issue超過due day 還被列在query 裡面，即送出email 給assignee。
    會產生一個excel "over_due_days.xlsx" 紀錄結果。
    :param url: query url
    :param cookies: redmine cookies
    :return: None
    """
    # 建立SMTP連線
    email_conn = smtplib.SMTP(host, port)
    # 試試看能否跟Gmail Server溝通
    print(email_conn.ehlo())
    # TTLS安全認證機制
    email_conn.starttls()
    # 登錄Gmail
    print(email_conn.login(username, password))
    table2 = setup(url, cookies) #呼叫setup 產生table dataframe
    print '----------Over Due Day----------'
    for i in range(0, table2.shape[0]): #table2.shape[0]: 計算出table dateframe 的row 數量。假如是table2.shape[1]: 計算出table dateframe 的column 數量
        """
        For loop遍巡整個table dataframe, 抓取due day 值來做此函式的核心判斷
        datess2: Column "over due day" 的值，經過處理會變成yyyy-mm-dd
        today: 利用date 函式產生的今日日期
        datesss2: 利用date 函式將datess2 轉成date 函式的資料型態
        oops2: 假如今日日期相減於due day 日期值，大於0表示超過due day，反之則表示還在due day範圍內
        """
        datess2 = str(table2.iloc[i, 8])#抓取 Column "Due Day" 值
        datess2 = datess2[0:10]
        datess2 = datess2.split('-')
        today = date.today()
        datesss2 = date(int(datess2[0]), int(datess2[1]), int(datess2[2]))
        oops2 = today - datesss2
        if oops2.days > 0:
            table2.iloc[i, 10] = 'True' #寫入值"True" 到Column "Over due day"
            issue_id2 = str(table2.iloc[i,0]) #抓取 issue id
            assignee2 = str(table2.iloc[i,5]) #抓取assignee
            to_list2 = [get_mail(issue_id2, assignee2, cookies)] #利用get_mail() 抓取assignee 的email
            print issue_id2, assignee2, to_list2 #列印結果
            subject = 'Issue %s was not updated over due days.' % (issue_id2) #email的 subject
            body = "Please pay attention to verify issue#%s. \n\nReminding from OGD Redmine. Please don't reply this mail." % (issue_id2) #email內容
            email_text = """Subject: %s

            %s
            """%(subject, body)
            #email_text 是寄出信件的內容格式宣告範例
            email_conn.sendmail(from_email, to_list2, email_text) # 寄信
            """
            email_conn.sendmail(from_email, to_list2, email_text) 裡面的"to_list2" 是處理過後的assignee的email
            假如剛開始使用這程式時想先測試功能，可將變數 "to_list2" 換成 "to_list" -> email_conn.sendmail(from_email, to_list, email_text)
            這樣可先將信送到一開始設定的測試email address。可以避免一開始送一堆測試信擾民。
            """
        else:
            table2.iloc[i, 10] = 'False' #假如還未超過due day, 則給值 "False"

    table2.to_excel('over_due_days.xlsx') #結果寫入excel
    email_conn.quit() #斷開 SMTP server連結

def over_three_day(url = query_url, cookies = cookies):
    """
    以Updated day為基準，假如issue超過3天還未更新，即送出email 給assignee。
    會產生一個excel "over_three_days.xlsx" 紀錄結果。
    :param url: query url
    :param cookies: redmine cookies
    :return: None
    """
    # 建立SMTP連線
    email_conn = smtplib.SMTP(host, port)
    # 試試看能否跟Gmail Server溝通
    print(email_conn.ehlo())
    # TTLS安全認證機制
    email_conn.starttls()
    # 登錄Gmail
    print(email_conn.login(username, password))
    table2 = setup(url, cookies)
    print '----------Over Three Day----------'
    for i in range(0, table2.shape[0]):
        """
        For loop遍巡整個table dataframe, 抓取Updated 值來做此函式的核心判斷
        oops2: 假如今日日期相減於due day 日期值，大於3表示超過3天沒更新，反之則表示還未超過3天
        """
        datess2 = str(table2.iloc[i, 6]) #抓取 Column "Updated" 值
        datess2 = datess2[0:10]
        datess2 = datess2.split('-')
        today = date.today()
        datesss2 = date(int(datess2[0]), int(datess2[1]), int(datess2[2]))
        oops2 = today - datesss2
        if oops2.days > 3:
            table2.iloc[i, 9] = 'True'
            issue_id2 = str(table2.iloc[i,0])
            assignee2 = str(table2.iloc[i,5])
            to_list2 = [get_mail(issue_id2, assignee2, cookies)]
            print issue_id2, assignee2, to_list2
            subject = 'Issue %s was not updated over three days.' % (issue_id2)
            body = "Please pay attention to verify issue#%s. \n\nReminding from OGD Redmine. Please don't reply this mail." % (issue_id2)
            email_text = """Subject: %s

            %s
            """ % (subject, body)
            # 寄信
            email_conn.sendmail(from_email, to_list2, email_text)

        else:
            table2.iloc[i, 9] = 'False'

    table2.to_excel('over_three_day.xlsx')
    email_conn.quit()

def over_days(url = query_url, cookies = cookies):
    """
    over_due_day() 與 over_three_day() 的綜合。
    會產生一個excel "over_days.xlsx" 紀錄結果。
    :param url: query url
    :param cookies: redmine cookies
    :return: None
    """
    # 建立SMTP連線
    email_conn = smtplib.SMTP(host, port)
    # 試試看能否跟Gmail Server溝通
    print(email_conn.ehlo())
    # TTLS安全認證機制
    email_conn.starttls()
    # 登錄Gmail
    print(email_conn.login(username, password))
    table2 = setup(url, cookies)
    print '----------Over Three Day----------'
    for i in range(0, table2.shape[0]):
        datess2 = str(table2.iloc[i, 6])
        datess2 = datess2[0:10]
        datess2 = datess2.split('-')
        today = date.today()
        datesss2 = date(int(datess2[0]), int(datess2[1]), int(datess2[2]))
        oops2 = today - datesss2
        if oops2.days > 3:
            table2.iloc[i, 9] = 'True'
            issue_id2 = str(table2.iloc[i,0])
            assignee2 = str(table2.iloc[i,5])
            to_list2 = [get_mail(issue_id2, assignee2, cookies)]
            print issue_id2, assignee2, to_list2
            subject = 'Issue %s was not updated over three days.' % (issue_id2)
            body = "Please pay attention to verify issue#%s. \n\nReminding from OGD Redmine. Please don't reply this mail." % (issue_id2)
            email_text = """Subject: %s

            %s
            """ % (subject, body)
            # 寄信
            email_conn.sendmail(from_email, to_list2, email_text)

        else:
            table2.iloc[i, 9] = 'False'

    print '----------Over Due Day----------'
    for i in range(0, table2.shape[0]):
        datess2 = str(table2.iloc[i, 8])
        datess2 = datess2[0:10]
        datess2 = datess2.split('-')
        today = date.today()
        datesss2 = date(int(datess2[0]), int(datess2[1]), int(datess2[2]))
        oops2 = today - datesss2
        if oops2.days > 0:
            table2.iloc[i, 10] = 'True'
            issue_id2 = str(table2.iloc[i, 0])
            assignee2 = str(table2.iloc[i, 5])
            to_list2 = [get_mail(issue_id2, assignee2, cookies)]
            print issue_id2, assignee2, to_list2
            subject = 'Issue %s was not updated over due days.' % (issue_id2)
            body = "Please pay attention to verify issue#%s. \n\nReminding from OGD Redmine. Please don't reply this mail." % (issue_id2)
            email_text = """Subject: %s

            %s
            """ % (subject, body)
            # 寄信
            email_conn.sendmail(from_email, to_list2, email_text)

        else:
            table2.iloc[i, 10] = 'False'

    table2.to_excel('over_day.xlsx')
    email_conn.quit()


if __name__ == '__main__':
    """
    在函式前面加上#號可以關掉不執行，假如想執行就將#拿掉即可
    """
    # over_due_day()
    # over_three_day()
    over_days()
