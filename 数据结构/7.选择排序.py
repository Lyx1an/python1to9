"""选择排序"""


def select_sort(alist):
    n = len(alist)
    # 需要进行 n-1 次操作
    for j in range(0, n - 1):
        # 记录最小的位置
        min_index = j
        # 从 j+1 到末尾，选出最小的数字
        for i in range(j + 1, n):

            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist

if __name__ == "__main__" :
    test_list = [ 22,313,4,5,76,43,2,3,32,5,15]
    result = select_sort(test_list)
    print(f"result is : {result}")