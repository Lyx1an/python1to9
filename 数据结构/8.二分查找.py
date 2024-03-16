
def binary_search(alist, item):
    n = len(alist)
    mid = n // 2
    if n > 0:
        if  alist[mid] == item:
            return True
        elif alist[mid] < item:
            return binary_search(alist[0:mid],item)
        else:
            return binary_search(alist[mid+1:], item)
    return False

if __name__ == "__main__" :
    # 测试案例
    test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(binary_search(test_list, 11))  # 输出 True
    print(binary_search(test_list, 8))  # 输出 False