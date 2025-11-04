# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

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

def primefactor(num):
    prime = []
    n = 2
    while n*n<=num:
        while num%n==0:
            prime.append(n)
            num = num//n
        n = n + 1
    if num!=1:
        prime.append(num)
    return prime


def solve():
    n,step = map_int()
    temp = primefactor(n)

    if len(temp)<step:
        print(-1)
        return
    first = temp[:step-1]
    last = [1]
    for j in range(step-1,len(temp)):
        last[0] = last[0] * temp[j]
    first.extend(last)
    print(*first)





def main():
    solve()

if __name__ == "__main__":
    main()