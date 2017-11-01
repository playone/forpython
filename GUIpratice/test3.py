#encoding: utf-8

from Tkinter import *

def colorChecked():
    label.configure(fg = color.get())

def typeChecked():
    textType = typeBold.get()+typeItalic.get()
    if textType == 1:
        label.configure(font = ('Arial', 12, 'bold'))
    elif textType == 2:
        label.configure(font = ('Arial', 12, 'italic'))
    elif textType == 3:
        label.configure(font = ('Arial', 12, 'bold italic'))
    else:
        label.configure(font = ('Arial', 12))


root = Tk()
root.title('Radio and Check test')

label = Label(root, text='Check the format of text', height=3, font=('Arial', 12))
label.pack(side = TOP)

color = StringVar()
Radiobutton(root, text='Red', variable = color, value = 'red', command=colorChecked).pack(side=LEFT)
Radiobutton(root, text='Blue', variable = color, value = 'blue', command=colorChecked).pack(side=LEFT)
Radiobutton(root, text='Green', variable = color, value='green', command=colorChecked).pack(side=LEFT)

typeBold = IntVar()
typeItalic = IntVar()
Checkbutton(root, text='Bold', variable = typeBold, onvalue=1, offvalue=0, command=typeChecked).pack(side=LEFT)
Checkbutton(root, text='Italic', variable = typeItalic, onvalue=2, offvalue=0, command=typeChecked).pack(side=LEFT)

root.mainloop()