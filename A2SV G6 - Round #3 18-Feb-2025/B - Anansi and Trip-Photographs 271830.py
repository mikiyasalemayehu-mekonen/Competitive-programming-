# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

n = int(input())
for _ in range(n):
    num , k =map(int,input().split())
    heights = list(map(int,input().split()))
    heights.sort()
    left = 0
    right =num
    yes_no = "YES"
    while left<num and right<num*2:
        if heights[right] - heights[left] <k:
            yes_no = "NO"
        left = left + 1
        right = right + 1
    print(yes_no)