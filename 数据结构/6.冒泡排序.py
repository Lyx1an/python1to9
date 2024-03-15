def bubble_sort(alist):
    n = len(alist)
    # 控制走多少次
    for j in range(0, n - 1):
        count = 0
        # 控制从头走到尾的距离
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            return alist
if __name__ == "__main__" :
    test_list = [2,45,65,21,12,5,4,36,2,213]
    result = bubble_sort(test_list)
    print(f"排序后的列表：{result}")
