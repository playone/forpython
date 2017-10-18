<<<<<<< HEAD
# encoding: utf-8

"""
I/O
檔案讀取 print 還有函式write
"""

import sys

file_in = file('db2.txt', 'r')
file_out = file('copy.txt', 'w')

for line in file_in:
    for i in range(0, len(line)):
        if line[i] != '\n':
            sys.stdout.write(line[i]+',')
        else:
            sys.stdout.write(line[i])
        file_out.write(line[i])

sys.stdout.write('\n')
file_in.close()
=======
# encoding: utf-8

"""
I/O
檔案讀取 print 還有函式write
"""

import sys

file_in = file('db2.txt', 'r')
file_out = file('copy.txt', 'w')

for line in file_in:
    for i in range(0, len(line)):
        if line[i] != '\n':
            sys.stdout.write(line[i]+',')
        else:
            sys.stdout.write(line[i])
        file_out.write(line[i])

sys.stdout.write('\n')
file_in.close()
>>>>>>> 14652bc9844615e043475427cc0564a4f5227e2a
file_out.close()