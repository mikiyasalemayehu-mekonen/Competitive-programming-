# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

from itertools import accumulate


n = int(input())
for _ in range(n):
    r = int(input())
    red = list(map(int,input().split()))
    b = int(input())
    blue = list(map(int,input().split()))
    max_red = max(0,max(list(accumulate(red))))
    max_blue = max(0,max(list(accumulate(blue))))
    print(max_blue+max_red)