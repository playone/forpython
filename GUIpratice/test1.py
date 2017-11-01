#encoding: utf-8

"""
這篇主要練習框架的排版, 會繼續研讀
"""



from Tkinter import *
import ttk


def main():
    root = Tk()

    content = ttk.Frame(root, padding=(3, 3, 12, 12))
    frame = ttk.Frame(
        content, borderwidth=7, relief='solid', width=200, height=100)
    namelbl = ttk.Label(content, text='Name')
    name = ttk.Entry(content)

    onevar = BooleanVar()
    twovar = BooleanVar()
    threevar = BooleanVar()

    onevar.set(True)
    twovar.set(False)
    threevar.set(True)

    one = ttk.Checkbutton(content, text='one', variable=onevar, onvalue=True)
    two = ttk.Checkbutton(content, text='two', variable=twovar, onvalue=True)
    three = ttk.Checkbutton(
        content, text='three', variable=threevar, onvalue=True)

    ok = ttk.Button(content, text='OK')
    cancel = ttk.Button(content, text='Cancel')

    content.grid(column=0, row=0, sticky=(N, S, E, W))
    frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
    namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
    name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
    one.grid(column=0, row=3)  # row=2 seems the same
    two.grid(column=1, row=3)
    three.grid(column=2, row=3)
    ok.grid(column=3, row=3)
    cancel.grid(column=4, row=3)

    # when the window resized, all widget will be resized, too

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=3)
    content.columnconfigure(1, weight=3)
    content.columnconfigure(2, weight=3)
    content.columnconfigure(3, weight=1)
    content.columnconfigure(4, weight=1)
    content.rowconfigure(1, weight=1)

    root.mainloop()

if __name__ == '__main__':
    main()