#!/usr/bin/python3

#随机生成1-10000之间无序序列整数数据
import random


def generator():
     random_data = []
     for i in range(1, 10):
        random_data.append(random.randint(1, 1000))
        random.randint
        print(i)
     return  random_data
    #冒泡排序
def bubble_sort(datalist):
        #获取序列长度
     length = len(datalist)
     for i in range(0,length):
            for j in range(i+1,length):
                if datalist[i] > datalist[j]:
                    datalist[i],datalist[j] = datalist[j],datalist[i]#数据交换
     return  datalist
if __name__ == "__main__":
    print("冒泡排序开始;")
    #生成随机数
    random_data = generator()
    print(random_data)
    #插入数据排序
    sort_data = bubble_sort(random_data)
    print(sort_data)
    print("冒泡排序结束")