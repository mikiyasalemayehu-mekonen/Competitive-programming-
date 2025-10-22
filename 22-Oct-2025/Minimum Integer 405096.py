# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

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
        l,r,d = map_int()
        tem1 = l%d
        tem2 = r%d
        if  d<l:
            print(d)
        elif tem2==0:
            print(r+d)
        else:
            print(r - tem2 + d)

def main():
    solve()

if __name__ == "__main__":
    main()