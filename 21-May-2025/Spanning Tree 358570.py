# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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
    n, m = map_int()
    edges = []
    for i in range(m):
        b,w,e = map_int()
        edges.append((b,w,e))
    edges = sorted(edges,key=lambda x:x[2])
    parent = {i:i for i in range(1,n+1)}
    size = [-1]+[1]*n
    def get(x):
        if parent[x]!=x:
            x = get(parent[x])
        return x
    def union(x,y):
        parent_x = get(x)
        parent_y = get(y)
        if size[parent_x]>=size[parent_y]:
            parent[parent_y] = parent_x
            size[parent_x] = size[parent_x] + 1
        else:
            parent[parent_x] = parent_y
            size[parent_y] = size[parent_y] + 1
    ans = 0
    for u,v,a in edges:
        if get(u)!=get(v):
            union(u,v)
            ans = ans + a
    print(ans)





def main():
    solve()

if __name__ == "__main__":
    main()
