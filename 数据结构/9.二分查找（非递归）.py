def binary_search_2(alist, item):
    """二分查找——非递归"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last) // 2
        if alist[mid] == item:
            return True
        # 如果 目标值 在右侧，将last等于中间值的左侧第一个
        elif item < alist[mid]:
            last = mid - 1
        # 如果在左侧，将first等于中间值右边第一个
        else:
            first = mid + 1
    return False