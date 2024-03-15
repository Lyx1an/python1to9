class Queue():
    """队列"""
    def __init__(self):
        self.__list = []

# 由于队列是先进先出，所以实际操作中，需要考虑进的多，还是出的多。
# 根据这个，来选择针对列表的插入和查询的时间复杂度
    def enqueue(self, item):
        """往队列尾部中插入一个元素"""
        self.__list.append(item)

    def dequeue(self):
        """从头部头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())