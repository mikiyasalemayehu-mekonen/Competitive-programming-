# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

from itertools import accumulate


n = int(input())
stones = list(map(int,input().split()))
prefix_sum = list(accumulate(stones))
stones.sort()
sorted_prefix_sum = list(accumulate(stones))
m = int(input())
for _ in range(m):
    t,l,r = map(int,input().split())
    if t==1 and l-2>=0:
        print(prefix_sum[r-1]-prefix_sum[l-2])
    elif t==1:
        print(prefix_sum[r-1])
    if t==2 and l-2>=0:
        print(sorted_prefix_sum[r-1]-sorted_prefix_sum[l-2])
    elif t==2:
        print(sorted_prefix_sum[r-1])
