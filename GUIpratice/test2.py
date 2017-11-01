#encoding: utf-8

"""
輸入框的練習
利用轉換溫度，來做使用者輸入，計算轉換跟顯示的練習
"""

from Tkinter import *
from ttk import *

def button_click():
    cd = float(entryCd.get()) #讀取使用者輸入，此時值為字串，需要用float()做轉換
    label.configure(text = '%.2f C = %.2f F' %(cd, cd*1.8+32)) #列印出結果在視窗上


root = Tk() #宣告主視窗
root.title('Entry Test') #主視窗的title

MainFrame = Frame(root, height=100, width=100) #宣告主框架，會將各個widgt放到此框架中
MainFrame.pack_propagate(0)
MainFrame.pack(padx = 150, pady = 100)

label = Label(MainFrame, text='Convert C to F...', width = 20)
label.pack()
entryCd = Entry(MainFrame, text = 'C')
entryCd.pack()
button_Cal = Button(MainFrame, text = 'Calculate', command = button_click)
button_Cal.pack()
root.mainloop()