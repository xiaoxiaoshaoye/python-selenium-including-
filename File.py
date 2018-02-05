# coding=utf-8
import  math
import pickle
import os
def hello():
    print('Hello World')

str = 'erw wrr3r   Hello8888888,' \
      '' \
      '' \
      '' \
      '' \
      'Worldrer r          '
# print(repr(str))

str1 = '123123124'
# print(str.rjust(20))
# print(str.center(220))
# print(str1.zfill(9))
# print('12'.zfill(3))
# print('PI的值是：%f'%math.pi)

f = open("C:/Users/dujuan/Desktop/CID.txt","r+")
# f.write('')
f.close()
f1 = open("C:/Users/dujuan/Desktop/CID.txt","r+")
str2 = f1.read()
print(str2)
str3 = f1.readline(0)
print(str3)
print(f1.tell())

f.close()



# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('C:/Users/dujuan/Desktop/1.pk1', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# output.close()#必须先关闭文件，不然会出现EOFError: Ran out of input错误
pkl_file = open('C:/Users/dujuan/Desktop/1.pk1','rb')
# data1 = pickle.load(pkl_file)
# print(data1)
pkl_file.close()



