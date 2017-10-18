<<<<<<< HEAD
# encoding: utf-8

"""
set 是集合運算 可以進行交集 連集 差集等運算
"""

admins = set()
users = {'smile', 'apple', 'mars', 'mark', 'emily'}
admins.add('hope')
admins.add('mars')

print admins & users
print admins | users
print admins ^ users
print admins - users
=======
# encoding: utf-8

"""
set 是集合運算 可以進行交集 連集 差集等運算
"""

admins = set()
users = {'smile', 'apple', 'mars', 'mark', 'emily'}
admins.add('hope')
admins.add('mars')

print admins & users
print admins | users
print admins ^ users
print admins - users
>>>>>>> 14652bc9844615e043475427cc0564a4f5227e2a
print users - admins