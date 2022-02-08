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
        a = []
        q.enqueue(tn)
        while not q.is_empty():
            a.append(q.peek().data)
            if q.peek().left is not None:
                q.enqueue(q.peek().left)
            if q.peek().right is not None:
                q.enqueue(q.peek().right)
            q.dequeue()
        return a

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

    def delete_node(self, n, data):
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

    def inorder_stack(self, n):
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

    def binary_search_tree_pre_order_traversal_iterative(self, tn) -> list:
        st = list()  # empty stack1
        res = list()
        st.append(tn)
        while True:
            v = st.pop()
            res.append(v.data)
            if v.right is not None:
                st.append(v.right)
            if v.left is not None:
                st.append(v.left)
            if len(st) == 0:
                break
        return res

    def binary_search_tree_post_order_traversal_iterative(self, tn) -> list:
        st = list()  # empty stack1
        res = list()
        st.append(tn)
        while True:
            v = st.pop()
            res.append(v.data)
            if v.right is not None:
                st.append(v.left)
            if v.left is not None:
                st.append(v.right)
            if len(st) == 0:
                break
        return res[::-1]

    def binary_search_tree_level_order_traversal(self, tn):
        q = Queue()
        a = []
        q.enqueue(tn)
        while not q.is_empty():
            r = []
            v = False
            q2 = Queue()
            while not q.is_empty():
                r.append(q.peek().data)
                if q.peek().left is not None:
                    q2.enqueue(q.peek().left)
                    v = True
                else:
                    q2.enqueue(TreeNode('n'))
                if q.peek().right is not None:
                    q2.enqueue(q.peek().right)
                    v = True
                else:
                    q2.enqueue(TreeNode('n'))

                q.dequeue()
            if not v:
                break
            q = q2
            a.append(r)
        a.append(r)
        return a

    def find_successor(self, root, val):
        if root is None:
            return None
        if root.left is not None and root.data > val:
            v = self.find_successor(root.left, val)
            if (v == -1 or v is None) and root.data > val:
                v = root.data
            return v
        if root.right is not None and root.data < val:
            v = self.find_successor(root.right, val)
            if (v == -1 or v is None) and root.data > val:
                v = root.data
            return v
        if root.data == val:
            if root.right is not None:
                return self.min_element_in_bst_recursion(root.right)
            return -1

    def find_predecessor(self, root, val):
        if root is None:
            return None
        if root.left is not None and root.data > val:
            v = self.find_predecessor(root.left, val)
            if (v == -1 or v is None) and root.data < val:
                v = root.data
            return v
        if root.right is not None and root.data < val:
            v = self.find_predecessor(root.right, val)
            if (v == -1 or v is None) and root.data < val:
                v = root.data
            return v
        if root.data == val:
            if root.left is not None:
                return self.max_element_in_bst(root.left)
            return -1

    def delete_node(self, root, value):
        if root.data == value:

            if root.left is None and root.right is None:

                return None
            elif root.left is None or root.right is None:
                if root.left is None:
                    return root.right
                elif root.right is None:

                    return root.left
            else:
                s = self.find_successor(root, value)
                self.delete_node(root, s)
                root.data = s
                root.set_smallest()
                return root
        if root.left is not None and root.data > value:

            root.left = self.delete_node(root.left, value)

            root.set_smallest()
            return root
        if root.right is not None and root.data < value:
            root.right = self.delete_node(root.right, value)
            root.set_smallest()
            return root

    def insertion_augmented(self,root,value):
        if root is None:
            root = AugmentedTreeNode(value)
        if root.data > value:
            root.left = self.insertion_augmented(root.left,value)
            root.set_smallest()
        elif root.data < value:
            root.right = self.insertion_augmented(root.right, value)
            root.set_smallest()
        return root


if __name__ == '__main__':
    bst = BinarySearchTree()
    a = AugmentedTreeNode(8)
    a = bst.insertion_augmented(a, 3)
    a = bst.insertion_augmented(a, 10)
    a = bst.insertion_augmented(a, 1)
    a = bst.insertion_augmented(a, 4)
    bst.delete_node(a, 8)
    bst.delete_node(a, 1)




