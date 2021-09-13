class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, ar=[], counter =-1):
        self.ar = ar
        self.counter = -1

    def is_empty(self):
        return self.counter == -1

    def push(self, data):
        self.ar.append(data)
        self.counter += 1

    def peek(self):
        if self.is_empty():
            return "No values are there to pop: Stack Underflow"
        return self.ar[self.counter]

    def pop(self):
        if self.is_empty():
            return "No values are there to pop: Stack Underflow"
        i = self.ar.pop(self.counter)
        self.counter -= 1
        return i

    def is_full(self):
        return self.counter > 100


class StackUsingLinkedList:
    def __init__(self, head: SinglyNode = None):
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
        if self.is_empty():
            return "No values are there to pop: Stack Underflow"
        i=self.head.data
        self.head=self.head.next
        return i
    def peek(self):
        if self.is_empty():
            return "No values are there to pop: Stack Underflow"
        return self.head.data
class minStack:
    def __init__(self, st: Stack = None , min: int=None):
        self.st = Stack()
        self.min = None
    def is_empty(self):
        return self.st.is_empty()
    def push(self,data):
        if self.min is None:
            self.st.push(data)
            self.min = data
            return
        if self.min < data:
            self.st.push(data)
        elif self.min >= data:
            dummy = 2*data - self.min
            self.min = data
            self.st.push(dummy)
    def pop(self):
        if self.is_empty():
            return "No values are there to pop: Stack Underflow"
        if self.min <= self.st.peek():

            return self.st.pop()
        elif self.min > self.st.peek():
            i = self.min

            self.min =2*self.min - self.st.peek()
            self.st.pop()
            return i

    def get_min(self):
        if self.st.is_empty():
            return "No values are there to pop: Stack Underflow"
        return self.min

    def peek(self):
        if self.st.is_empty():
            return "No values are there to pop: Stack Underflow"
        return self.st.peek()

if __name__ == '__main__':
    st=minStack()
    st.push(4)
    st.push(2)
    st.push(1)
    st.push(3)


    print(st.get_min())
    st.pop()
    print(st.get_min())
    st.pop()
    print(st.get_min())
    st.pop()
    print(st.get_min())
