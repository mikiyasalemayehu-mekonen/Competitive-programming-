# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from typing import Counter


t =  int(input())
for _ in range(t):
    n,k,d = map(int,input().split())
    series = list(map(int,input().split()))
    ptr1 = 0
    minimum = n
    val = {}
    for i in range(len(series)):
        val[series[i]] = val.get(series[i],0) + 1
        if i - ptr1 + 1 == d:
            minimum = min(minimum,len(val.keys()))
            val[series[ptr1]] = val[series[ptr1]] - 1
            if val[series[ptr1]] ==0:
                del val[series[ptr1]]
            ptr1 = ptr1 + 1
        else:
            continue
        
    print(minimum)

