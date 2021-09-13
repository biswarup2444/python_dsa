def longest_substring_without_repeating_char(s: str) -> int:
    a = 0
    b = a
    st = set()
    sum = 0
    while b < len(s) and a < len(s):
        if s[b] not in st:
            st.add(s[b])
            b += 1
        else:
            sum = max(len(st), sum)
            st.remove(s[a])
            a += 1
        print(st)
    sum = max(len(st), sum)
    return sum


def maximumUniqueSubarray(nums) -> int:
    st = set()
    a = 0
    b = 0
    lsum = 0
    gsum = 0
    while b < len(nums) and a < len(nums):
        if nums[b] not in st:
            st.add(nums[b])
            lsum += nums[b]
            gsum = max(lsum, gsum)
            b += 1
        else:
            st.remove(nums[a])
            lsum -= nums[a]
            a += 1

    s1 = 0
    for i in st:
        s1 += i
    return max(gsum, s1)


def seperate_one_and_zero(ar):
    j = 0
    for i in range(0, len(ar)):
        if ar[i] == 0:
            ar[i], ar[j] = ar[j], ar[i]
            j += 1
    return ar


def binary_addition(a, b):
    large = a
    small = b
    if len(b) > len(a):
        large = b
        small = a
    for i in range(len(small), len(large), 1):
        small = '0' + small
    c = 0
    s = ""
    for i in range(len(small) - 1, -1, -1):
        sum = c + int(large[i]) + int(small[i])
        s = str(sum % 2) + s
        c = sum // 2
    if c == 1:
        s = '1' + s
    return s


if __name__ == '__main__':
    a = list(range(9 // 2))
    print(a)
