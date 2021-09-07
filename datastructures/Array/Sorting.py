def bubble_sort(ar):
    for i in range(0, len(ar) - 1):
        for j in range(0, len(ar) - 1 - i):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]


def insertion_sort(ar):
    for i in range(1, len(ar)):
        v = ar[i]
        j = i
        while j > 0 and ar[j-1] > ar[j]:
            ar[j-1], ar[j] = ar[j], ar[j-1]
            j -= 1
        ar[j] = v


def selection_sort(ar):
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if ar[i]>ar[j]:
                ar[i],ar[j]=ar[j],ar[i]

def merge_sort(ar):
    if len(ar) == 1:
        return ar
    l = ar[:len(ar) // 2]
    r = ar[len(ar) // 2:len(ar)]
    l = merger_sort(l)
    r = merger_sort(r)
    ar = merger(l, r)
    return ar


def merge(ar1, ar2):
    ar3 = []
    size = min(len(ar1), len(ar2))
    i = 0
    j = 0
    while i < len(ar1) and j < len(ar2):
        if ar1[i] > ar2[j]:
            ar3.append(ar2[j])
            j += 1
        elif ar2[j] > ar1[i]:
            ar3.append(ar1[i])
            i += 1

    if len(ar1) > i:
        for a in range(i, len(ar1), 1):
            ar3.append(ar1[a])
    if len(ar2) > j:
        for a in range(j, len(ar2), 1):
            ar3.append(ar2[a])
    return ar3


def quick_sort(ar, s, e):
    if s < e:
        p_index = partiation(ar, s, e)
        quick_sort(ar, s, p_index - 1)
        quick_sort(ar, p_index + 1, e)


def partiation(ar, s, e):
    pivot = ar[e]
    p_index = s
    for i in range(s, e, 1):
        if ar[i] <= pivot:
            ar[i], ar[p_index] = ar[p_index], ar[i]
            p_index += 1

    ar[p_index], ar[e] = ar[e], ar[p_index]
    return p_index


def binary_search(ar: list[int], s: int, e: int, target: int) -> bool:
    print("new call\t start:\t", s, "end\t", e)
    if s >= e:
        return False
    if ar[(s + e) // 2] == target:
        return True
    elif ar[(s + e) // 2] > target:
        e = (s + e) // 2
        return binary_search(ar, s, e, target)
    elif ar[(s + e) // 2] < target:
        s = (s + e) // 2
        return binary_search(ar, s, e, target)
