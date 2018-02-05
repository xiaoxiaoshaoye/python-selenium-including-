#!/usr/bin/python3
import  random
# 随机生成1-10之间无序序列整数数据
"""
希尔排序属于插入类排序,是将整个有序序列分割成若干小的子序列分别进行插入排序。

排序过程：

先取一个正整数d1<n，把所有序号相隔d1的数组元素放一组，组内进行直接插入排序；
然后取d2<d1，重复上述分组和排序操作；
直至di=1，即所有记录放进一个组中排序为止。
"""
def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data


# 希尔排序
def shell_sort(data_list):
    # 序列长度
    length = len(data_list)
    # 步长，这个数据大家可以修改下，查看排序过程
    step = 2
    # 分组
    group = int(length / step)
    print("gourp: ", group)
    while group > 0:
        # 遍历分组，对所有分组进行排序
        for i in range(0, group):
            j = i + group
            # 对分组进行排序
            while j < length:
                k = j - group
                key = data_list[j]
                while k >= 0:
                    if data_list[k] > key:
                        data_list[k + group] = data_list[k]
                        data_list[k] = key
                    k = k - group
                j = j + group

        group = int(group / step)

    return data_list


if __name__ == "__main__":

    # 生成随机无序数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 排序
    length = len(random_data)
    sorted_data = shell_sort(random_data)

    # 打印排序结果
    print(sorted_data)