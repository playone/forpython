#encoding: utf-8

"""
河內塔練習
"""


def hanoi(n, A, B, C):
    if n == 1:
        return [(A, C)]
    else:
        return hanoi(n-1, A, C, B) + hanoi(1, A, B, C) + hanoi(n-1, B, A, C)

count = 0
n = input("請輸入整數：")
for move in hanoi(int(n), 'A', 'B', 'C'):
    count += 1
    print ('第 %i 步' %count)
    print("盤由 %c 移至 %c" % move)


print ('總步數: %i' %count )
