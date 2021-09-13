from linkedlist.singly.sinlgy_node import *
def kadnes_algorithim(ar):
    local_max = -100000
    global_max = ar[0]
    for i in ar:
        local_max=max(i,local_max+i)
        global_max=max(global_max,local_max)
    return global_max
def negative_elements_group(ar):
    i=0
    j=len(ar)-1
    while i<=j:
        if ar[i]<0:
            i+=1
        elif ar[i]>=0 and ar[j]<0:
            temp=ar[i]
            ar[i]=ar[j]
            ar[j]=temp
            i+=1
            j-=1
        elif ar[i]:
            j-=1
        print(str(i)+"\t"+str(j))
    return ar
def lengthOfLongestSubstring(s) :
    if len(s)==0 or len(s)==1:
        return len(s)
    st = ""
    m = 0
    for i in range(0 , len(s)-1 , 1):
        st = ""+s[i]
        for j in range(i+1 , len(s) , 1):

            if st.find(s[j]) != -1:
                m = max(m, len(st))
                break
            st = st + s[j]
        m = max(m , len(st))
    return m
def longest_palindrome_substring(s):
    v=0
    st=""
    for i in range(len(s)):
        t=""
        for j in range(i+1,len(s)+1,1):
            t=s[i:j]
            if (len(t)>len(st)) and isPlaindrome(t):
                st=t
    return st

def rorate_by_k(ar,n,k):
    k = k % n
    gc = gcd(n , k)
    for i in range(gc):
        temp = ar[i]
        j = i
        while True:
            d = j - k
            if d < 0 :
                d = n + d
            if d == i:
                break
            ar[j] = ar[d]
            j = d
        ar[j] = temp
    return ar
def rotate_by_k_brute_force_clockwise(ar,n,k):
    for i in range(k):
        x=ar[n-1]
        y = ar[0]
        for i in range(0,n-1):
            b=ar[i+1]
            ar[i+1]=y
            y=b
        ar[0]=x
    return ar
def rotate_by_k_brute_force_anti_clockwise(ar,n,k):
    k=k%n
    for i in range(k):
        x=ar[0]
        y=ar[n-1]
        for j in range(1,n):
            ar[j-1]=ar[j]
        ar[n-1]=x
    return ar
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def isPlaindrome(s):
    return s==s[::-1]
def digit_count(n):
    a=[]
    n=abs(n)
    while n>0:
        r=n%10
        if r in a:
            return 0
        a.append(r)
        n=n//10
    return 1

def unique_numbers(l,r):
    c=0
    for i in range(abs(l),abs(r+1)):
        c=c+digit_count(i)
    return c


def pascal_triangle(n):
    r1=list(list())
    for i in range(n):
        r=[]
        for j in range(i+1):
            r.append(combination(i,j))
        r1.append(r)
    return r1

def combination(n,r):
    c=factorial(n)//(factorial(n-r)*factorial(r))
    return c

def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
if __name__ == '__main__':
    ar=[3,3,2,1,6,5,8,4]

    print(selection_sort(ar))
    print(ar)
