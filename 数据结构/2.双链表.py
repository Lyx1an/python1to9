# 构造节点
class Node():
    def __init__(self, elem):
        self.elem = elem
        # 前驱节点
        self.prev = None
        # 后继节点
        self.next = None


# 构造链表
class SingleLinkList():
    # 初始化链表（默认为空链表）
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表的长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # 记录数量
        count = 0
        while cur != None:
            count += 1
            # 将游标赋给下一个
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            # 打印游标指向的节点
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部增加元素"""
        node = Node(item)
        node.next = self.__head
        if self.__head:
            self.__head.prev = node
        self.__head = node

    def append(self, item):
        """链表尾部增加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                # 移动游标，当下一个为None，退出循环，当前的cur为最后一个节点
                cur = cur.next
            cur.next = node
            node.prev = cur

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
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 当循环退出时，cur指向pos位置
            node = Node(item)
            # node的next指向cur所在位置，即插入值的下一个值
            node.next = cur
            # node的prev指向node的前一个值
            node.prev = cur.prev
            # node的前一个值的next指向node
            cur.prev.next = node
            # 插入值的下一个值的prev指向node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        # 被删除元素位置的前一个节点
        pre = None
        while cur != None:
            if cur.elem == item:
                # 判断此节点是否为头节点
                if cur == self.__head:
                    self.__head = cur.next
                    # 如果头节点不是None
                    if cur.next:
                        # 判断该链表是否只有一个节点
                        cur.next.prev = None
                else:
                    # 目标值的前一个节点的next指向后一个节点
                    cur.prev.next = cur.next
                    if cur.next:
                        # 目标值的后一个节点的prev指向前一个节点
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
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