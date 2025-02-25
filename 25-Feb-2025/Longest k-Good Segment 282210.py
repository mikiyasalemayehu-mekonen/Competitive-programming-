# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

n , k  = map(int,input().split())
nums = list (map(int,input().split()))


elements = {} 
left = 0
max_length = 0 
best_left, best_right = 0, 0  

for right in range(n):
    elements[nums[right]] = elements.get(nums[right], 0) + 1

    while len(elements) > k:
        elements[nums[left]] -= 1
        if elements[nums[left]] == 0:
            del elements[nums[left]] 
        left += 1 

    if right - left + 1 > max_length:
        max_length = right - left + 1
        best_left, best_right = left, right

print(best_left + 1, best_right + 1)

