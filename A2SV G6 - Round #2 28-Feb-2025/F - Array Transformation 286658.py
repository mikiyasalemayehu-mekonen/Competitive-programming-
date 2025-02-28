# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F


from collections import Counter


n = int(input())
for _ in range(n):
    size = int(input())
    nums = list(map(int,input().split()))
    minimum = size
    count = Counter(nums)
    max_count = max(count.values())
    freq = list(set(count.values()))
    for num in freq:
        temp = 0
        for key,value in count.items():
            if value <num:
                temp = temp + value 
            elif value>num:
                temp = temp + value - num
        minimum = min(minimum,temp)
                
    print(minimum)
