#encoding: utf-8

from Tkinter import *
from ttk import *

def button_click():
    cd = float(entryCd.get())
    label.configure(text = '%.2f C = %.2f F' %(cd, cd*1.8+32))


root = Tk()
root.title('Entry Test')

MainFrame = Frame(root, height=100, width=100)
MainFrame.pack_propagate(0)
MainFrame.pack(padx = 150, pady = 100)

label = Label(MainFrame, text='Convert C to F...', width = 20)
label.pack()
entryCd = Entry(MainFrame, text = 'C')
entryCd.pack()
button_Cal = Button(MainFrame, text = 'Calculate', command = button_click)
button_Cal.pack()
root.mainloop()