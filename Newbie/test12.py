# encoding: utf-8

"""
可以用import 導入python 檔裡面整個函式
或者用from '檔案' import '函式' 來導入特定的函式
"""

import sys #導入 sys 底下所有的函式, 使用sys裡面的write 函式前面需要加檔名

from time import time #從 time 檔案裡面導入 time 函式, 使用此函式前面不用加檔名


sys.stdout.write(str(time())+'\n')
