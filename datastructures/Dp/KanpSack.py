from typing import List

mem = [0] * 50
mem = mem * 50


def knap_sack(wt, val, w: int, n: int) -> int:
    if n == 0 or w <= 0:
        return 0
    if wt[n - 1] <= w:
        return max(val[n - 1] + knap_sack(wt, val, w - wt[n - 1], n - 1), knap_sack(wt, val, w, n - 1))
    elif wt[n - 1] > w:
        return knap_sack(wt, val, w, n - 1)


def knap_sack_meomzie(wt, val, w: int, n: int):
    if n == 0:
        return 0
    if mem[w][n] == -1:
        return mem[w][n]
    if wt[n - 1] <= w:
        mem[w][n] = max(val[n - 1] + knap_sack(wt, val, w - wt[n - 1], n - 1), knap_sack(wt, val, w, n - 1))
        return mem[w][n]
    elif wt[n - 1] > w:
        mem[w][n] = knap_sack(wt, val, w, n - 1)
        return mem[w][n]


def knap_sack_td(wt, val, w: int, n: int):
    m = [[0 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j >= wt[i - 1]:
                m[i][j] = max(val[i - 1] + m[i - 1][j - wt[i - 1]], m[i - 1][j])
            else:
                m[i][j] = m[i - 1][j]
    return m[n][w]


def equal_sum_parittion(arr) -> bool:
    n = len(arr)
    s = 0
    for each in arr:
        s += each
    if s % 2 != 0:
        return False
    s = s % 2
    m = [[None for i in range(s + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(s + 1):
            if i == 0 or j == 0:
                m[i][j] = 0
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if j < arr[i - 1]:
                m[i][j] = max(arr[i - 1] + m[i - 1][j - arr[i - 1]], m[i - 1][j])
            else:
                m[i][j] = m[i - 1][j]
    return m[n][s] == s


def count_subset_sum(arr: List[int], s: int) -> int:
    n = len(arr)
    c = 0
    m = [[0 for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if j==0:
                m[i][j] = 1
    print(m)
    for i in range(1,n+1):
        for j in range(1,s+1):
            if j>=m[i][j]:
                m[i][j]=m[i-1][j-arr[i-1]]+m[i-1][j]
            else:
                m[i][j]=m[i-1][j]
    c=m[n][s]

    return c


if __name__ == '__main__':
    ar = [2,3,5,6,8,10]
    print(count_subset_sum(ar,10))
