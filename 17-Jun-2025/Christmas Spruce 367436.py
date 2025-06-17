# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

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
    graph = defaultdict(list)
    for i in range(2, t + 1):
        pi = int(in_str()) 
        graph[pi].append(i)
    
    def is_spruce():
        for node in range(1, t + 1):
            if len(graph[node]) > 0:  
                leaf_count = 0
                for child in graph[node]:
                    if len(graph[child]) == 0:  
                        leaf_count += 1
                if leaf_count < 3:  
                    return False
        return True

    print("Yes" if is_spruce() else "No")
def main():
    solve()

if __name__ == "__main__":
    main()
