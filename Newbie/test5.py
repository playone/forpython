# encoding: utf-8

"""
字串可用 " 或者 ' 做區隔
同時字串也是利用陣列的概念作存取
"""

s = "hello"
s += 'world'
s1 = s.replace('l', "1")
s2 = s[0]+"i"

print s, s1, s2

"""
內建的字串分割函式 spilt非常好用，可以將字串依指定字元做切割
"""

s3 = 'I have a pen'
s3_split=s3.split(' ')

print s3_split