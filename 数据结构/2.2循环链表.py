# 构造节点
class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None


# 构造链表
class SingleLinkList():
    # 初始化链表（默认为空链表）
    def __init__(self, node=None):
        self.__head = node
        # 如果是只有一个节点，需要next区域指向他自身
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表的长度"""
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历节点
        cur = self.__head
        # 记录数量
        count = 1
        while cur.next != self.__head:
            count += 1
            # 将游标赋给下一个
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        if self.is_empty():
            return
        while cur.next != self.__head:
            # 打印游标指向的节点
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环， cur指向尾节点，但尾节点没有打印
        print(cur.elem)

    def add(self, item):
        """链表头部增加元素"""
        node = Node(item)
        if self.is_empty():
            # 空链表，头部指向node
            self.__head = node
            # next区域指向自身
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环，cur指向尾节点
            # node的next指向下一个值
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self, item):
        """链表尾部增加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node


    def insert(self,pos, item):
        """指定位置插入元素
        :param pos 从0开始
        """
        # 空链表
        if pos <= 0:
            self.add(item)
        # 插入值的位置大于链表长度-1，证明在链表末尾
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count =0
            # 当循环的次数小于插入指定位置的参数-1，那么当前为要插入位置的前一个位置
            while count < (pos-1):
                count += 1
                pre = pre.next
            node = Node(item)
            # 将目标数的next区域指向下一个的值
            node.next = pre.next
            # 将前一个位置的next指向插入值
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        # 被删除元素位置的前一个节点
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                # 判断此节点是否为头节点
                if cur == self.__head:
                    # 头节点情况
                    # 尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 将前一个的next指向当前游标的next的指向（即下一个值）
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False

if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)

    print(ll.is_empty())
    print(ll.length())

    ll.add(8)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.travel()

    ll.insert(7, 10)
    ll.travel()

    ll.remove(1)
    ll.travel()