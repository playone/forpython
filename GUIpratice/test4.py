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

cvs.create_line(150, 0, 50, 400)
cvs.create_line(100, 50, 200, 300, fill='red', dash=(4, 4), arrow=LAST)

cvs.create_rectangle(200, 50, 400, 200, fill='blue')

cvs.create_oval(450, 50, 550, 200, fill='green')
drawCircle(cvs, 400, 300, 50, fill='red')

cvs.create_polygon(200, 250, 350, 250, 350, 350, 220, 300, fill='yellow')

root.mainloop()