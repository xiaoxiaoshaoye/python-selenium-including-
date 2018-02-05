#!/usr/bin/env python3
# encoding: utf-8

import  sys


# a,b = 0,1
# while b < 10:
#     print(b,end=',')
#     a,b = b,a+b
#     print(a,end=',')

# age = int(input("请输入你家狗狗的年龄："))

# if age<0:
#     print("Are you kidding me")
# elif age==1:
#     print('相当于14岁的人')
# elif age == 2:
#     print('相当于22岁的人')
# elif age > 2:

    # human = 22+(age -2) *5
    # print('对应人类的年龄',human);


# n = 10
# sum = 0
# counter = 1
#
# while counter <= n:
#     sum = sum + counter
#     counter +=1
#
#     print(sum)
#
#
# count = 0
#
# while count < 5:
#     print(count,'小于5')
#     count += 1
# else:
#     print(count,'大于5')
#     sites = ['baidu','Google','Taobao','Weibo','QQ']
#
#     for site in  sites:
#         if site == 'baidu':
#             print('是百度')
#     else:
#         print('不是百度')
#
#
# for i in range(10):
    # print(i)

    # for i in  range(-30,-200,-40):
        # print(i)

        # for letter in 'Runoob':  # 第一个实例
            # if letter == 'n':
            #     pass
                # print('执行 pass 块')
                # break
            # print('当前字母为 :', letter)


list = [1,2,3,4]
it = iter(list)
print(next(it))
t = (1,23,34)
u = t,(312314,3423)
print(u)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('orange' in basket  )
print(basket)
basket1 = set('');
print(basket1)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q,a in zip(questions,answers):
        print(q,a)
        for i in reversed(range(1, 10, 2)):
            print(i)