class TreeNode:
    def __init__(self, data=0):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return self.data


class AugmentedTreeNode:
    def __init__(self, data=0):
        self.data = data
        self.right = None
        self.left = None
        self.smallest = data


    def set_smallest(self):
        if self.left is None:
            self.smallest = self.data
        else:
            self.smallest = self.left.smallest

class BinaryTree:
    def insert_left(self, n, data):
        if n is None:
            return TreeNode(data)
        n.left = self.insert_left(n.left, data)
        return n

    def insert_right(self, n, data):
        if n is None:
            return TreeNode(data)
        n.right = self.insert_right(n.left, data)
        return n
