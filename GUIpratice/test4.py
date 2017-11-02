#encoding: utf-8

"""
繪圖板練習
"""


from Tkinter import *

def drawCircle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

root = Tk()
root.title('Canvas Test')

cvs = Canvas(root, width = 600, height = 400)
cvs.pack()

cvs.create_line(150, 0, 50, 400) #(起點的X軸, 起點的Y軸, 終點的X軸, 終點的Y軸, fill = '顏色', dash 虛線, arrow 線的箭頭= LAST 終點, FIRST 起點, BOTH 兩邊 )
cvs.create_line(100, 50, 200, 300, fill='red', dash=(4, 4), arrow=BOTH)

cvs.create_rectangle(100, 100, 200, 200, fill='blue') #(方形的左上角X軸 方形的左上角Y軸 方形的右下角X軸 方形的右下角Y軸) 對角線的概念 由左上對到右下繪出方形

cvs.create_oval(250, 100, 350, 200, fill='green') # 圓形
drawCircle(cvs, 400, 300, 50, fill='red')

cvs.create_polygon(200, 250, 350, 250, 350, 350, 220, 300, fill='yellow') #四邊形

root.mainloop()