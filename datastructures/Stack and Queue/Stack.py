from . import singly_node

class Stack:
    def __init__(self, ar, counter):
        self.ar = ar
        counter = -1

    def is_empty(self):
        return counter == -1

    def push(self, data):
        ar.append(data)
        self.counter += 1

    def peek(self) -> int:
        return self.ar[self.counter]

    def pop(self) -> int:
        i = self.ar.remove(self.peek())
        self.counter -= 1
        return i

    def is_full(self):
        return self.counter > 100


class StackUsingLinkedList:
    def __init__(self, head: SinglyNode):
        self.head = head

    def is_empty(self):
        return self.head is None

    def push(self, data):
        if self.head is None:
            self.head = SinglyNode(data)
        else:
            tr = SinglyNode(data)
            tr.next = self.head
            self.head = tr

    def pop(self):
        if is_empty():
            return "No values are there to pop: Stack Underflow"
        i=self.head.data
        self.head=self.head.next
        return i

if __name__ == '__main__':
    st=StackUsingLinkedList()
    print(st.is_empty())