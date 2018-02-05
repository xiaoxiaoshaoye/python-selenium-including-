#!/usr/bin/python3
import  random
#随机生成1-10000之间无序序列整数数据
def generator():
     random_data = []
     for i in range(1, 10):
        random_data.append(random.randint(1, 1000))
        print(i)
     return  random_data
    #选择排序
    #每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完

def select_sort(data_list):
    length = len(data_list)
    for i in range(0,length):
        min = i
        #查找最小的元素
        for j in  range(0,length):
             if data_list[j] < data_list[min]:
                 min = j
        #交互位置
        data_list[min],data_list[i] = data_list[i],data_list[min]

    return  data_list

if __name__ =="__main__":
    random_data = generator()
    print("生成随机数")
    print(random_data)
    lergth = len(random_data)
    sorted_data = select_sort(random_data)
    print("排序后的数".join('%s' %id for id in sorted_data))
    # print(sorted_data)