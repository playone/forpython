<<<<<<< HEAD
# encoding: utf-8

"""
例外處理
"""

def my_divide():
    try:
        10 / 0
    except ZeroDivisionError:
        print '不能除以0'
    else:
        print '沒有任何錯誤'
    finally:
        print '無論有沒有錯誤都會執行這一行'

=======
# encoding: utf-8

"""
例外處理
"""

def my_divide():
    try:
        10 / 0
    except ZeroDivisionError:
        print '不能除以0'
    else:
        print '沒有任何錯誤'
    finally:
        print '無論有沒有錯誤都會執行這一行'

>>>>>>> 14652bc9844615e043475427cc0564a4f5227e2a
my_divide()