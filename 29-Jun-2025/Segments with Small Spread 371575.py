# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter

def in_str() -> str: return sys.stdin.readline().strip()
def t_int() -> int: return int(sys.stdin.readline().strip())
def map_int(): return map(int, sys.stdin.readline().strip().split())
def t_list() -> list: return list(map(int, sys.stdin.readline().strip().split()))
def in_strings(): return sys.stdin.readline().strip().split()
def in_string_list() -> list: return list(sys.stdin.readline().strip())
def in_matrix(n: int) -> list: return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

from collections import deque

def solve():
    n, k = map_int()
    nums = t_list()
    
    max_dq = deque() 
    min_dq = deque()  
    left = 0
    ans = 0

    for right in range(n):

        while max_dq and nums[right] > max_dq[-1]:
            max_dq.pop()
        max_dq.append(nums[right])

        while min_dq and nums[right] < min_dq[-1]:
            min_dq.pop()
        min_dq.append(nums[right])

    
        while max_dq[0] - min_dq[0] > k:
            if max_dq[0] == nums[left]:
                max_dq.popleft()
            if min_dq[0] == nums[left]:
                min_dq.popleft()
            left += 1

   
        ans += (right - left + 1)

    print(ans)


def main():
    solve()

if __name__ == "__main__":
    main()
