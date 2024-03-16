"""插入排序"""


def insert_sort(alist):
    n = len(alist)
    # 从第二个位置开始，即下标0，到n-1
    for i in range(1, n):
        # i, i-1, i-2 ,..., 1
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j - 1], alist[j] = alist[j], alist[j - 1]
            # 最优解，即 目标列表已经排好序
            else:
                break


"""插入排序"""


def insert_sort_2(alist):
    n = len(alist)
    # 从第二个位置开始，即下标0，到n-1
    for i in range(1, n):
        # i, i-1, i-2 ,..., 1
        j = i
        while j > 0:
            if alist[j] < alist[j - 1]:
                alist[j - 1], alist[j] = alist[j], alist[j - 1]
                j -= 1
            # 最优解，即 目标列表已经排好序
            else:
                break


l = [22, 44, 11, 22, 3, 14, 20]
print(l)
insert_sort(l)
print(l)
