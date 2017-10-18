
# encoding: utf-8

"""
排序
處理資料中最常使用的功能, python 提供好用的sorting 函式
lambda 是簡易型函式,只能傳回一個值, 因此如果需要兩個值以上的排序, 會用 attrgetter
"""

class student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def set_name(self, name):
        self.name = name

student_object = []
student_object.append(student('john', 'B', 10))
student_object.append(student('len', 'A', 11))
student_object.append(student('lin', 'C', 12))
for i in student_object:
    print i.name, i.grade, i.age
print

student_object.sort(key=lambda i: i.grade)
for i in student_object:
    print i.name, i.grade, i.age
print

from operator import attrgetter

student_object.sort(key=attrgetter('grade', 'age'), reverse=True)
for i in student_object:
    print i.name, i.grade, i.age

print