# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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
    size = [-1]+[1]*n
    parent=[i for i in range(n+1)]
    xp=[0 for i in range(n+1)]
    # size=[1 for i in range(n+1)]
    def find(x):
        if x !=parent[x]:
            return find(parent[x])
        return parent[x]

    def union(j,k):
        J=find(j)
        K=find(k)

        if K==J:
            return
        if size[K]<size[J]:
            size[J]+=size[K]
            xp[K]-=xp[J]
            parent[K]=J
        else:
            size[K]+=size[J]
            xp[J]-=xp[K]
            parent[J]=K

    def get(x,v):
        if x!=parent[x]:
            v += xp[parent[x]]
            return get(parent[x],v)
        return v 


    for _ in range(m):
        que= in_strings()
        if que[0]=='add':
            x=find(int(que[1]))
            xp[x]+=int(que[2])
        elif que[0]=='join':
            j=int(que[1])
            k=int(que[2])
            union(j,k)
        else:
            print(get(int(que[1]),xp[int(que[1])]))
         


         

def main():
  solve()

if __name__ == "__main__":
  main()
