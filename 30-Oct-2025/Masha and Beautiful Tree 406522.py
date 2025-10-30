# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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
        n = t_int()
        arr = t_list()
        count = 0
        flag = True
        def merge(left_half,right_half):
            nonlocal count,flag
            merged = sorted(left_half+ right_half)

            left = left_half + right_half
            right = right_half + left_half

            if merged == right and merged != left:
                count += 1
            elif merged != right and merged != left:
                flag = False

            return merged


        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = (left + right )//2

            left_half = mergeSort(left,mid,arr)
            right_half = mergeSort(mid+1,right,arr)

            return merge(left_half,right_half)


        nums = mergeSort(0,n-1,arr)
        if flag:
            print(count)
        else:
            print(-1)






def main():
    solve()

if __name__ == "__main__":
    main()