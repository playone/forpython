
# encoding: utf-8

"""
這程式是練習excel的讀取寫入
會用到函式 xlwt
"""

import xlwt

wb = xlwt.Workbook() #宣告一個excel

sh = wb.add_sheet('A new sheet') #新增一個sheet

#以下是寫入資料
sh.write(0, 0, 'hello100')
sh.write(1, 0, 'world')
sh.write(2, 0, 1234567)
sh.write(2, 1, '2017/10/17')

wb.save('xlwt_test.xls') #存檔