# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

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
    for i in range(t):
        word = list(input())
        a = ord(word[0]) -ord('a')

        b = ord(word[1]) - ord('a')
        if b<a:
            b = b +1
        print((a*25) + b)




def main():
    solve()

if __name__ == "__main__":
    main()