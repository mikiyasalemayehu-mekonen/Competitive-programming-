# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

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

def trial_division_simple(n):
    factorization = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.add(d)
            n //= d
        d += 1
    if n > 1:
        factorization.add(n)
    return len(factorization) == 2

def solve():
    n = t_int()

    
    cnt = 0
    for i in range(1,n+1):
        if trial_division_simple(i):
            cnt += 1
    print(cnt)


def main():
    solve()

if __name__ == "__main__":
    main()