# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
nums = list(map(int,input().split())) 
nums.sort()                   

prefix_sum = [0] * n
suffix_sum = [0] * n

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + (nums[i] - nums[i - 1]) * i

for i in range(n - 2, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + (nums[i + 1] - nums[i]) * (n - i - 1)
min_cost = float('inf')
best_index = 0

for i in range(n):
    total_cost = prefix_sum[i] + suffix_sum[i]
    if total_cost < min_cost:
        min_cost = total_cost
        best_index = i

print(nums[best_index])  
