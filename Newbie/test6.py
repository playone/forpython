<<<<<<< HEAD
# encoding: utf-8

"""
中文的處理 我們可以透過unicode 的編解碼來處理
"""

s = "台灣"
u = s.decode('utf8')

print '台', s[0], u[0] #S 沒有被解碼 所以執行完之後會無法被顯示
=======
# encoding: utf-8

"""
中文的處理 我們可以透過unicode 的編解碼來處理
"""

s = "台灣"
u = s.decode('utf8')

print '台', s[0], u[0] #S 沒有被解碼 所以執行完之後會無法被顯示
>>>>>>> 14652bc9844615e043475427cc0564a4f5227e2a
print u[0] == u'台'