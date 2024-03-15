class Deque():
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列头部中插入一个元素"""
        self.__list.insert(0 ,item)

    def add_rear(self, item):
        """尾部"""
        self.__list.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """尾部"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    s = Deque()
    s.add_front(1)
    s.add_front(2)
    s.add_front(3)
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())