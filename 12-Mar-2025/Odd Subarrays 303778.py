# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

#miki
def maps():
    return map(int,input().split())
n = int(input())
for _ in range(n):
    size = int(input())
    num = list(maps())
    count = 0
    i = 0
    while i <size-1:
        if num[i]>num[i+1]:
            count = count + 1
            i = i + 1
        i = i + 1
    print(count)
