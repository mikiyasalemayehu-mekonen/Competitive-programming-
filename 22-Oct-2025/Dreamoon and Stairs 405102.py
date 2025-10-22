# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

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
    n,m = map_int()
    if n<m:
        print(-1)
        return
    else:
        if n==m:
            print(n)
            return

        temp = n//2 
        cnt = temp
        temp = temp + 1 if n%2!=0 else temp
        while cnt!=0:
            if temp%m==0:
                print(temp)
                return
            temp = temp + 1
            cnt = cnt - 1
        print(-1)

    
    
    

def main():
    solve()

if __name__ == "__main__":
    main()