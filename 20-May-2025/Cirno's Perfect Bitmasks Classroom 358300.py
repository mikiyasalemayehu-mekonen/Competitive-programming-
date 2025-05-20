# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

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
def is_power_of(n, base):
    if base <= 1:
        return n == 1 if base == 1 else False
    power = 1
    while power < n:
        power *= base
    return power == n

def solve():
    t = t_int()
    for _ in range(t):
        n = int(input())
        bin_n = bin(n)[2:]
        ans = []
        xor = 1
        count_one = bin_n.count("1") 
        bin_n = bin_n.zfill(30)
        checked = False
        if n>1 and is_power_of(n,2):
            print(n+1)
            continue      
        for i in range(29,-1,-1):
            if bin_n[i]=="1":
                ans.append("1")
                count_one = count_one -1
                checked = True
                if count_one>0:
                    break
            elif xor==1 and bin_n[i]=="0" and count_one<=1 :
                ans.append("1")
                xor = xor - 1
                if xor==0  and checked:
                    break
            else:
                ans.append("0")

       
        ans.reverse()
        ans = "".join(ans)
        ans = ans.zfill(30)
        ans = int(ans,2)
        print(ans)

        

def main():
    solve()

if __name__ == "__main__":
    main()
