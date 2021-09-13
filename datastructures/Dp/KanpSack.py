def knap_sack(wt: list[int], val: list[int], w: int, n: int) -> int:
    if n == 0 or w <= 0:
        return 0
    if wt[n - 1] <= w:
        return max(val[n - 1] + knap_sack(wt, val, w - wt[n - 1], n - 1), knap_sack(wt, val, w, n - 1))
    elif wt[n - 1] > w:
        return knap_sack(wt, val, w, n - 1)



if __name__ == '__main__':
    for i in range(100):
        print(i, end=";")
