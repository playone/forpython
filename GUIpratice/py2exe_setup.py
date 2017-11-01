#encoding : utf-8

"""
利用py2exe來建置py檔的exe file
setups那邊
windows 是給視窗程式使用
console 是給非視窗程式使用
"""

from distutils.core import setup
import py2exe
from Tkinter import *
from ttk import *

setup(windows=['helloworld.py'])