#! python 2.7
#encoding: utf-8

"""
F3是資料 F4是關鍵字 F5是結果
利用F4 去搜尋F3 將結果存至F5
"""

with open('3.txt') as f3, open('4.txt') as f4, open('result.txt', 'a') as f5:
    a = [line.strip() for line in f4.readlines()]
    for li in f3.readlines():
        new_line = li.strip()
        for i in a:
            if i in new_line:
                f5.writelines(li)