#encoding: utf-8

"""
基本練習
建立視窗 建立Label 建立button 同時賦予button功用可執行
"""

from Tkinter import *
from ttk import *

count = 0
def click_ok():
    global count
    count += 1
    labal.configure(text='Click OK ' + str(count) + ' times')

win = Tk() #建立視窗容器物件
win.title('my first window title') #定義視窗title
labal = Label(win, text='Helloworld') #建立標籤物件
button = Button(win, text='OK', command=click_ok) #建立button物件, command定義button功能
labal.pack() #顯示元件
button.pack() #顯示元件
win.mainloop()

