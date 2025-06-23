# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

from bisect import bisect_left
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
        n, m = map_int()
        a = t_list()
        b = sorted(t_list())
        before = float("-inf")
        for j in range(n):
            tem =  a[j] + before
        
            idx = bisect_left(b,tem)
            options = []
            if a[j] >= before:
                options.append(a[j])
            if idx < m:
                changed = b[idx] - a[j]
                if changed >= before:
                    options.append(changed)


            if not options:
                print('NO')
                break
            before = min(options)
        else:
            print('YES')

        


def main():
    solve()

if __name__ == "__main__":
    main()
