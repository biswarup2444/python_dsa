from Queue import *
from Node import *


class BinarySearchTree:

    def insert(self, tn, data):
        if tn is None:
            tn = TreeNode(data)
        if tn.data > data:
            tn.left = self.insert(tn.left, data)
        elif tn.data < data:
            tn.right = self.insert(tn.right, data)
        return tn

    def search(self, tn, target):
        if tn is None:
            return False
        if tn.data == target:
            return True
        elif tn.data > target:
            return self.search(tn.left, target)
        else:
            return self.search(tn.right, target)

    def max_element_in_bst_recursion(self, tn):
        if tn is None:
            return "Empty tree"
        if tn.right is None:
            return tn.data
        return self.max_element_in_bst_recursion(tn.right)

    def min_element_in_bst(self, tn):
        if tn is None:
            return "Empty tree"
        while tn.left is not None:
            tn = tn.left
        return tn

    def min_element_in_bst_recursion(self, tn):
        if tn is None:
            return "Empty tree"
        if tn.left is None:
            return tn.data
        return self.min_element_in_bst_recursion(tn.left)

    def max_element_in_bst(self, tn):
        if tn is None:
            return "Empty tree"
        while tn.right is not None:
            tn = tn.right
        return tn

    def find_height_of_bst(self, tn):
        if tn is None:
            return -1
        left = self.find_height_of_bst(tn.left)
        right = self.find_height_of_bst(tn.right)
        return max(left, right) + 1

    def find_depth_of_node(self, data, root):
        if root is None:
            return -1
        if data == root.data:
            return 0
        if data > root.data:
            root = root.right
        else:
            root = root.left
        val = self.find_depth_of_node(data, root)
        if val == -1:
            return -1
        return val + 1

    def binary_search_tree_level_order_traversal(self, tn):
        q = Queue()
        q.enqueue(tn)
        while not q.is_empty():
            print(q.peek().data, end=" ")
            if q.peek().left is not None:
                q.enqueue(q.peek().left)
            if q.peek().right is not None:
                q.enqueue(q.peek().right)
            q.dequeue()

    def binary_search_tree_pre_order_traversal(self, tn):
        if tn is None:
            return
        print(tn.data, end=" ")
        self.binary_search_tree_pre_order_traversal(tn.left)
        self.binary_search_tree_pre_order_traversal(tn.right)

    def binary_search_tree_in_order_traversal(self, tn):
        if tn is None:
            return

        self.binary_search_tree_in_order_traversal(tn.left)
        print(tn.data, end=" ")
        self.binary_search_tree_in_order_traversal(tn.right)

    def binary_search_tree_post_order_traversal(self, tn):
        if tn is None:
            return
        self.binary_search_tree_post_order_traversal(tn.left)
        self.binary_search_tree_post_order_traversal(tn.right)
        print(tn.data, end=" ")

    def is_bst(self, n):
        if n is None:
            return True
        return self.is_bst(n.left) and self.is_bst(n.right) and self.is_less(n.left, n.data) and self.is_greater(
            n.right, n.data)

    def is_less(self, n, data):
        if n is None:
            return True
        return n.data < data and self.is_less(n.left, n.data) and self.is_greater(n.right, n.data)

    def is_greater(self, n, data):
        if n is None:
            return True
        return n.data > data and self.is_less(n.left, n.data) and self.is_greater(n.right, n.data)

    def delete_node(self,n ,data):
        if n is None:
            return n
        if data > n.data:
            n.right = self.delete_node(n.right, data)
            return n
        elif data < n.data:
            n.left = self.delete_node(n.left, data)
            return n
        else:
            if n.left is None and n.right is None:
                n = None
            elif n.left is None:
                n = n.right

            elif n.right is None:
                n = n.left
            else:
                d = self.min_element_in_bst(n.right)
                n.data = d.data
                n.right = self.delete_node(n.right, d.data)
            return n
    def inorder_stack(self,n):
        q = []
        cr = n
        a = []
        while True:
            if cr is not None:
                q.append(cr)
                cr = cr.left
            elif len(q) != 0:
                cr = q.pop()
                a.append(cr.data)
                cr = cr.right
            else:
                break
        return a

if __name__ == '__main__':
    a = TreeNode(3)
    bst = BinarySearchTree()
    a = bst.insert(a, 1)
    a = bst.insert(a, 5)
    a = bst.insert(a, 2)
    a = bst.insert(a, 0)
    a = bst.insert(a, 4)
    a = bst.insert(a, 6)
    bst.binary_search_tree_in_order_traversal(a)
    print(bst.inorder_stack(a))
