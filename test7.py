# encoding: utf-8

"""
型別轉換 基本運算符
python 不用特別宣告變數，所以要注意不能讓不同型態的變數同時運算
"""

x = 2**3
y = 3/2
s = '3'

print x, y, s
# x+s 會出錯 因為是 int+str 不同型態
print ord('a'), ord('c'), chr(ord('a')+2) # ord-字元轉編號 chr-編號轉字元
print y, int(s)/2, float(s)/2, 3%2
print str(x+y), str(x)+str(y)