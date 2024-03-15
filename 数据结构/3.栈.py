class Stack():
    """栈"""
    # 新定义一个私有列表作为容器
    def __init__(self):
        self.__list = []

    # 由于尾部插入的时间复杂度为O(1)，头部为O(n)，所以在尾部插入
    def push(self, item):
        """添加一个新的元素到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())