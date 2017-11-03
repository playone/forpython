#encoding: utf-8

"""
Calendar的lib 是從http://svn.python.org/projects/sandbox/trunk/ttk-gsoc/samples/ttkcalendar.py 下載放至tk lib裡
此篇是calendar的練習
"""

import Tkinter
import ttkcalendar

import tkSimpleDialog

def ok_clicked():
    result = calendar.selection #獲取選取日期的資料，此時資料型態是datetime
    result = str(result)        #將資料型態轉換成字串
    result = result[0:10]       #擷取自前面幾個所需字元 會顯示出 yyyy-mm-dd
    result = result.replace('-','/') #將字元 - 轉換成 /
    print ' ' in result         #判斷是否有某字元存在於字串
    print type(result)
    print result

root = Tkinter.Tk()
title = root.title('Calendar Test')

calendar = ttkcalendar.Calendar(root) #宣告calendar物件
calendar.pack()


button = Tkinter.Button(root, text = 'ok', command = ok_clicked)
button.pack()

root.mainloop()
"""
class CalendarDialog(tkSimpleDialog.Dialog):
    #Dialog box that displays a calendar and returns the selected date
    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection

# Demo code:
def main():
    root = Tkinter.Tk()
    root.wm_title("CalendarDialog Demo")

    def onclick():
        cd = CalendarDialog(root)
        print cd.result

    button = Tkinter.Button(root, text="Click me to see a calendar!", command=onclick)
    button.pack()
    root.update()

    root.mainloop()


if __name__ == "__main__":
    main()

"""