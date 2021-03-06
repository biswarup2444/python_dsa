class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, d):
        x = SinglyNode(d)

        if self.head is None:
            self.head = x
        else:
            x.next = self.head
            self.head = x

    def insert_at_tail(self, d):
        tr = self.head
        while tr.next is not None:
            tr = tr.next
        tr.next = SinglyNode(d)

    def is_empty(self):
        return self.head is None

    def print_all(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

    def print_all(self, tr):
        while tr is not None:
            print(tr.data)
            tr = tr.next

    def reverse_using_recusrion(self, h):
        if h.next is None:
            return h
        r = None
        r = self.reverse_using_recusrion(h.next)
        h.next.next = h
        h.next = None
        return r

    def reverse_using_loop(self, h):
        prev = None
        nxt = None

        while h is not None:
            nxt = h.next
            h.next = prev
            prev = h
            h = nxt
        return prev

    def remove_without_head_brute_force(self, h):
        tr = h
        while (tr.next is not None):
            tr.data = tr.next.data
            tr = tr.next
        while (h.next != tr):
            h = h.next
        h.next = None

    def delete_without_head_simple(self, h):
        if h is None or h.next is None:
            return None
        x = h.next.next
        h.data = h.next.data
        h.next = x


def remove_loop(h):
    slow = h
    fast = h
    tr = h

    while fast.next is not None:

        fast = fast.next
        if fast is None:
            break
        fast = fast.next
        slow = slow.next
        if fast == slow:
            break

    while slow.next != tr.next:
        tr = tr.next
        slow = slow.next

    slow.next = None
    return h



