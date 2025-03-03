# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

# from collections import defaultdict


# n = int(input())
# for _ in range(n):
#     size , k = map(int,input().split())
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     temp_a  = sorted(a)
#     temp_b = sorted(b)
#     sorted_pair = defaultdict(list)
#     for a1 ,b1 in zip(temp_a,temp_b):
#         sorted_pair[a1].append(b1)
#     ans = []
#     i = 0
#     checked = set() 
#     while i<size and len(ans)<size:
#         if a[i] in checked:
#             i = i + 1
#             continue
#         checked.add(a[i])
#         temp = sorted_pair[a[i]]
#         for j in range(len(temp)):
#             ans.append(temp[j])
#         i = i+ 1

#     print(*ans)
from collections import defaultdict


n = int(input())
for _ in range(n):
    size , k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    temp_a  = sorted(a)
    temp_b = sorted(b)
    sorted_pair = defaultdict(list)
    for a1 ,b1 in zip(temp_a,temp_b):
        sorted_pair[a1].append(b1)
    ans = []
    i = 0
    while i<size :
        ans.append(sorted_pair[a[i]].pop())
        i = i+ 1
    print(*ans)
    
 
 
