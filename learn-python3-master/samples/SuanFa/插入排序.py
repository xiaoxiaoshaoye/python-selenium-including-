#!/usr/bin/python3
import random
#生成随机数
def generator():
    random_data = [];
    for i in  range(0,10):
        random_data.append(random.randint(1,1000))
    return  random_data
#插入排序
#插入排序的基本操作是将一个数据插入到已经排序好的有序序列中，从而获得一个新的有序序列。

#插入排序适合什么样的场景？

#适合数据量相对较小的排序需求场景。其时间复杂度为：O（n^2），是一种稳定的排序方法。
def insertSort(data_list):
     #序列长度
     length = len(data_list)
     for i in range(1,length):
         key = data_list[i]#插入的数据
         j = i-1
         print("开始插入排序888888")
         while j>=0:
             #插入排序
              if data_list[j]>key:
                  data_list[j+1] = data_list[j]
                  data_list[j]=key
                  print("开始插入排序9999999")
              j = j - 1
     return data_list

if __name__ == "__main__":
    print("开始插入排序")
    random_data = generator()
    print("原始数据：")
    print(random_data)
    sorted_data = insertSort(random_data)
    print("开始插入排序2222222")
    print(sorted_data)
    print(sorted_data)