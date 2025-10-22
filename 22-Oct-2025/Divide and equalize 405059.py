# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

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
    
    def trial_division_simple(n,factors):
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors[d] = factors.get(d, 0) + 1
                n //= d
            d += 1
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
        return factors

    t = t_int()
    for i in range(t):
        n = t_int()  
        nums = t_list()
        factors = {}
        for num in nums:
            factors = trial_division_simple(num,factors)
        if not factors:
            print("YES")
            continue
        values = sum(factors.values())
        for key in factors:
            if factors[key] % n != 0:
                print("NO")
                break

        else:
           
            print("YES")
     

    
    
    

def main():
    solve()

if __name__ == "__main__":
    main()