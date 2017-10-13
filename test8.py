# encoding: utf-8

"""
流程控制 判斷式和迴圈
每個流程的結尾都是:
在Python裡面不用括號 而是用縮排來區別
縮排對於程式閱讀非常有幫助
Python對於縮排要求非常嚴格
在IDE裡面在tab的設定是使用後退4個space

在PYTHON的判斷式中 and, or, not 是邏輯運算子
也提供了一個好用的函式 rangee，範圍是從左邊數字到右邊數字-1，撰寫迴圈會更加快速
IN 函式  可以用來判斷某個型別中是否有某個元素
"""

mylist = []

for i in range(0,10): # i = 0; i<10; i++
    mylist.append(i+1) #把for迴圈裡面的-1 加回來
print mylist

if mylist[0] == 1 and len(mylist)<10: #第一個條件有符合可是第二個條件沒達成
    mylist[0] += 1
    print '1 state'
elif (10 in mylist) or not(len(mylist) == 10): #elif = else if. 第一個條件達成 第二個條件不符合 可是因為是OR 所以此判斷式通過
    print '2 state'
    print 'range(i, j) is i~j-1'
else:
    print '3 state'
    print 'None of above'

for i in mylist: # i=0; i<=mylist.length(); i++
    print i, # cout<<mylist[i]
print
