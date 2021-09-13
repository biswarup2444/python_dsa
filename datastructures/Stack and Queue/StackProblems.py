from queue import LifoQueue


def largestRectangleArea(heights):
    nr = nsr(heights)
    nl = nsl(heights)
    s = 0
    for i in range(len(heights)):
        s = max(s, heights[i] * ((abs(nr[i] - nl[i])) - 1))
    return s

def nsr(n):
    q = []
    a = []
    for i in range(len(n) - 1, -1, -1):
        if len(q) == 0:
            a.append(len(n))
        elif q[-1] != len(n) and n[q[-1]] < n[i]:
            a.append(q[-1])
        elif n[q[-1]] >= n[i]:
            while len(q) != 0 and n[q[-1]] >= n[i]:
                q.pop()
            if len(q) == 0:
                a.append(len(n))
            else:
                a.append(q[-1])
        q.append(i)
    return a[::-1]


def nsl(n):
    q = []
    a = []
    for i in range(0, len(n), 1):
        if len(q) == 0:
            a.append(-1)
            #q.append(i)
        elif q[-1] != -1 and n[q[-1]] < n[i]:
            a.append(q[-1])
            #q.append(i)
        elif n[q[-1]] >= n[i]:
            while len(q) != 0 and n[q[-1]] >= n[i]:
                q.pop()
            if len(q) == 0:
                a.append(-1)
            else:
                a.append(q[-1])
        q.append(i)
    return a


ar = [1,1]
print(nsr(ar))
print(nsl(ar))
print(largestRectangleArea(ar))
