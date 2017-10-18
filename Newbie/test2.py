
# encoding: utf-8

"""
python的list 是可變動大小的陣列
可透過append增加
也有許多好用的函式
"""

mylist = []
mylist.append(1)
mylist.append(2)
mylist2 = [5.5, "hi", 3, 99, 222, 222]
print mylist2[0]
mylist2[0]= 333.333

print len(mylist), sum(mylist), mylist2.count(222)
print mylist2[0], mylist2[-1], mylist2[1:3], mylist2[2:]


