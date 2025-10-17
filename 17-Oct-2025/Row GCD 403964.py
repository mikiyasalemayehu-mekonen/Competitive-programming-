# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

import sys
from math import gcd
from collections import defaultdict, Counter

def in_str() -> str: return sys.stdin.readline().strip()
def t_int() -> int: return int(sys.stdin.readline().strip())
def map_int(): return map(int, sys.stdin.readline().strip().split())
def t_list() -> list: return list(map(int, sys.stdin.readline().strip().split()))
def in_strings(): return sys.stdin.readline().strip().split()
def in_string_list() -> list: return list(sys.stdin.readline().strip())
def in_matrix(n: int) -> list: return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

def solve():
    n, m = map_int()
    num1 = t_list()
    num2 = t_list()

    G = 0
    for i in range(1, n):
        G = gcd(G, abs(num1[i] - num1[0]))
    res = [str(gcd(G, num1[0] + b)) for b in num2]

    print(" ".join(res))

def main():
    solve()

if __name__ == "__main__":
    main()
