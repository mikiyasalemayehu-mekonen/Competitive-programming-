# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque

def in_str() -> str: return sys.stdin.readline().strip()
def t_int() -> int: return int(sys.stdin.readline().strip())
def map_int(): return map(int, sys.stdin.readline().strip().split())
def t_list() -> list: return list(map(int, sys.stdin.readline().strip().split()))
def in_strings(): return sys.stdin.readline().strip().split()
def in_string_list() -> list: return list(sys.stdin.readline().strip())
def in_matrix(n: int) -> list: return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

def solve():
    n, k = map_int()
    nums = t_list()

    max_q = deque()
    min_q = deque()
    left = 0
    result = 0

    for right in range(n):
        while max_q and nums[max_q[-1]] <= nums[right]:
            max_q.pop()
        max_q.append(right)

        while min_q and nums[min_q[-1]] >= nums[right]:
            min_q.pop()
        min_q.append(right)

        while nums[max_q[0]] - nums[min_q[0]] > k:
            if max_q[0] == left:
                max_q.popleft()
            if min_q[0] == left:
                min_q.popleft()
            left += 1

        result += (right - left + 1)

    print(result)

def main():
    solve()

if __name__ == "__main__":
    main()
