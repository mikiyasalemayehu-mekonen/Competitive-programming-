# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

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

def solve():
    t = t_int()
    for _ in range(t):
        n, k = map_int()
        colors = list(input())
        penalty = t_list()
        if "B" not in  colors:
            print(0)
            continue
        
        def check(mid):
            oprs = 0
            paint = False
            for i in range(n):
                if penalty[i] > mid:
                    if not paint and colors[i] == "B":
                        paint =True
                        oprs += 1
                    elif paint and colors[i] == "R":
                        paint = False
            return oprs <= k

        low = 0
        high = max(penalty)
        ans = 0
        while low<=high:
            mid = (low+high)//2
            if check(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        print(ans)


def main():
    solve()

if __name__ == "__main__":
    main()
