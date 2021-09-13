class Queue:
    def __init__(self):
        self.ar = []
        self.s = -1
        self.e = -1

    def is_empty(self):
        return (self.s == -1 and self.e == -1) or self.s > self.e

    def enqueue(self, data):
        self.ar.append(data)
        if self.is_empty():
            self.s += 1
            self.e += 1
        else:
            self.e += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        data = self.ar[self.s]
        self.s += 1
        return data
    def peek(self):
        if self.is_empty() :
            return "Queue is empty"
        return self.ar[self.s]
