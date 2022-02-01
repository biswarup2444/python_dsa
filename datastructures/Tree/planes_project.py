'''A runway reservation system we are designing such that we can add planes to be landed on the runway as long as there are no planes
scheduled to land within k mins for the plane to land, we also have to determine the number of planes that would be landing on the runway before
a certain time'''


class augmented_binary_tree_node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
        self.limit = 3


class augmented_tree_node_size:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
        self.rank = 1
        self.limit = 3


class opeartions:
    def runway_reservation(self, root, time):
        if abs(root.key - time) < root.limit:
            return "Reservation unsuccessful."
        else:
            if root.key > time:
                if root.left is not None:
                    return self.runway_reservation(root.left, time)
                else:
                    root.left = augmented_binary_tree_node(time, None, None)
                    return "Reservation successful."
            else:
                if root.right is not None:
                    return self.runway_reservation(root.right, time)
                else:
                    root.right = augmented_binary_tree_node(time, None, None)
                    return "Reservation successful."

    def insertion_with_new_size(self, root, value):
        if abs(root.key - value) < root.limit:
            return "Reservation unsuccessful."
        else:
            if root.key < value:
                if root.right is not None:
                    self.insertion_with_new_size(root.right, value)
                elif root.right is None:
                    root.right = augmented_tree_node_size(value, None, None)
                root.rank += 1
                return "Reservation successful."
            if root.key > value:
                if root.left is not None:
                    self.insertion_with_new_size(root.left, value)
                elif root.left is None:
                    root.left = augmented_tree_node_size(value, None, None)
                root.rank += 1
                return "Reservation successful."



if __name__ == '__main__':
    n = augmented_tree_node_size(5, None, None)
    op = opeartions()
    print(n.rank)
    op.insertion_with_new_size(n, 1)
    print(n.rank)
    op.insertion_with_new_size(n, 8)
    print(n.rank)
    print(op.insertion_with_new_size(n, 3))
    print(n.rank)
    print(op.insertion_with_new_size(n, 11))



