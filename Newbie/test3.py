<<<<<<< HEAD
# encoding: utf-8

"""
Dictionary像是Hash table一樣 一個key對應一個變數
"""

passwd = {'mars':00000, 'mark':56789}
passwd['happy']=9999
passwd['smile']=123456

del passwd['mars']
passwd['mark']=passwd['mark']+1

print passwd
print passwd.keys()
print passwd.get('tony')
=======
# encoding: utf-8

"""
Dictionary像是Hash table一樣 一個key對應一個變數
"""

passwd = {'mars':00000, 'mark':56789}
passwd['happy']=9999
passwd['smile']=123456

del passwd['mars']
passwd['mark']=passwd['mark']+1

print passwd
print passwd.keys()
print passwd.get('tony')
>>>>>>> 14652bc9844615e043475427cc0564a4f5227e2a
print passwd.get('smile')