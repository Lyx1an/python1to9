class Node():
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree():
    """二叉树"""

    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            # 节点指针，从第一个开始
            cur_node = queue.pop(0)
            # 如果左节点的子节点为None，就赋值给他；否则 末尾追加
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            # 只有当队列为空时，才将新节点添加为右子节点
            if cur_node.rchild is None and not queue:
                cur_node.rchild = node
                return
            elif cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    # '''-------------------------------树的遍历------------------------------------------'''
    def breath_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            # 打印指针的元素
            print(cur_node.elem, end=" ")
            # 如果左子节点不为空，就进行 添加
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        else:
            print(node.elem, end=" ")
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        else:
            self.inorder(node.lchild)
            print(node.elem, end=" ")
            self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        else:
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.elem, end=" ")
