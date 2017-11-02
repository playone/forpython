#encoding: utf-8

from Tkinter import *
from tkMessageBox import *

def btn1_clicked():
    showinfo('info', 'showinfo test')

def btn2_clicked():
    showwarning('Warning', 'showWarning test')

def btn3_clicked():
    showerror('Error', 'showError test')

def btn4_clicked():
    askquestion('Question', 'AskQuestion Test')

def btn5_clicked():
    askokcancel('OkCancel', 'OkCancel Test')

def btn6_clicked():
    askyesno('YesNo', 'YesNo Test')

def btn7_clicked():
    askyesnocancel('YesNoCancel', 'YesNoCancel Test')

def btn8_clicked():
    askretrycancel('RetryCancel', 'RetryCancel Test')


root = Tk()
title = root.title('Messagebox test')

btn1 = Button(root, text = 'show info', command = btn1_clicked)
btn1.pack(fill=X)
btn2 = Button(root, text = 'show warning', command = btn2_clicked)
btn2.pack(fill=X)
btn3 = Button(root, text = 'show error', command = btn3_clicked)
btn3.pack(fill=X)
btn4 = Button(root, text = 'Ask Question', command = btn4_clicked).pack(fill=X)
btn5 = Button(root, text = 'Ok Cancel', command = btn5_clicked).pack(fill=X)
btn6 = Button(root, text = 'Yes No', command = btn6_clicked).pack(fill=X)
btn7 = Button(root, text = 'Yes No Cancel', command = btn7_clicked).pack(fill=X)
btn8 = Button(root, text = 'Retry Cancel', command = btn8_clicked).pack(fill=X)

root.mainloop()
