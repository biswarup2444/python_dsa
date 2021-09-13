class TreeNode:
    def __init__(self, data=0):
        self.data = data
        self.right = None
        self.left = None


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
