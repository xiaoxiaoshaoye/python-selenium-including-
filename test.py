#!/usr/bin/env python3
# encoding: utf-8

# print("Hello World",end="")
#
# print("""则会使一饿,多行显示,哈哈哈哈""")
# print("word")
#
# print("   ")


# 执行完这局之后，按Enter键才会执行下边的操作
# input("\n\n按下 enter 键后退出。")

# 导入模块
# import  sys
# 导入特定模块
import  math
import  random

import File

import sys

import fibo
from fibo import  *
import  using_name

import


# from sys import argv

# print('参数个数为：',len(sys.argv),'个参数')

File.hello()
print(sys.path)

fib(10)
fib2(3)
print(dir(fibo))
print(dir(sys))

x =testClass ()
print(x)

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

# print(counter)
# print(miles)
# print(name)

a,b,c=1,4,'hahh'
# print(a,b,c)
# print(type(a))
# print(type(c))
# print(isinstance(a,int))
var1 = 10

# print(var1)

del var1

# str = 'fdsgfdgdfh'
# print(str[0:5])
# print(str * 2)
# print(str+'Tzet')
# print('fsg\nffsf')
# print('Ru\noob')
# print(r'ru\nhi')

list=['1','2','3','4','5','6']
# print(list)
# print(list[0])
#
# print(list[1:3])
# print(list[2:])
# print(list[0:9])

tuple = ('1','2','3','4','5','6','70')
tinytuple = ('hahah','二号')
# print(tuple)
# print(tuple[0:2])
# print(tuple[1:6])
# print(tinytuple * 2)
# print(tinytuple+tuple)

# 集合，无序，去掉重复元素
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)
# if('Jessie' in student):
    # print('Rose在集合中')
# else:
    # print('Rose不在集合中')

c = set('fffgweeq')
# print(c)
d = set('gjhjgk')

# print(c - d)
# print(c | d)
# print(c^ d)
# print(c & d)

dict = {'name':'runboob','sex':'female','age':23}
# print(dict)
# print(dict['sex'])
#
# print(dict.fromkeys('123156','d'))
# print(dict.keys())
# print(dict.values())
'''

'''

"""
f = 2
g = str(dict)
print(str(tuple))


d =2
print(d**6)

h = 34
print(h/d)

print(h%d)

print(h//d)

if(h != d):

    print('相等')
else:
    print('不相等')


c = 0
# c += d
c = d&h

c = h or d
# print(c)
"""
a = 10
b = 20
list = [1, 2, 3, 4, 5];


# if (a in list):
#     print("1 - 变量 a 在给定的列表中 list 中")
# else:
#     print("1 - 变量 a 不在给定的列表中 list 中")
#
# if (b not in list):
#     print("2 - 变量 b 不在给定的列表中 list 中")
# else:
#     print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
# a = 2
# if (a in list):
#     print("3 - 变量 a 在给定的列表中 list 中")
# else:
#     print("3 - 变量 a 不在给定的列表中 list 中")
#
# a = 20
# b = 20

# if (a is b):
#     print("1 - a 和 b 有相同的标识")
# else:
#     print("1 - a 和 b 没有相同的标识")
#
# if (id(a) == id(b)):
#     print("2 - a 和 b 有相同的标识")
# else:
#     print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
# b = 30
# if (a is b):
#     print("3 - a 和 b 有相同的标识")
# else:
#     print("3 - a 和 b 没有相同的标识")
#
# if (a is not b):
#     print("4 - a 和 b 没有相同的标识")
# else:
#     print("4 - a 和 b 有相同的标识")

"""
width=-20
height=10
print(width/height)
print(abs(width))
print(math.fabs(width))
"""

print(random.random())

print(math.e)
print(math.pi)


print("字符串")

print("我叫%s。今年%d岁"%('嘟嘟',28))

str02 = "this is string example from runoob....wow!!!"

# print ("str.capitalize() : ", str02.capitalize())

list2 = [1, 2, 3, 4, 5, 6, 7 ];
# print(list2[1:7])

list_copy = list2.copy()
# print("copy的列表：",list_copy)
list_copy.append(2)
# print(list_copy)
# print(max(list_copy))
list_copy.insert(6,9)
print(list_copy)




list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
# print ('列表插入元素后为 : ', list1)
tup1 = (50,)
print(type(tup1))


dict03 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# dict02 = {'user':'yunwei','pwd':'12334'}
# print(str(dict03))
# print(dict03.keys())
# print(dict03.values())
# # print(dict03.clear())
# print(dict03.get('Age'))
# print(dict03.items())
# print(dict03.setdefault('Sex','Male'))
# print(dict03)
# dict03.update(dict02)
# print(dict03)



