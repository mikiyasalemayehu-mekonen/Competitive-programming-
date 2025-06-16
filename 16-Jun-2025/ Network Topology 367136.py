# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B


import sys
from collections import defaultdict, deque

def in_str() -> str: return sys.stdin.readline().strip()
def t_int() -> int: return int(sys.stdin.readline().strip())
def map_int(): return map(int, sys.stdin.readline().strip().split())
def t_list() -> list: return list(map(int, sys.stdin.readline().strip().split()))

def solve():
    n, m = map_int()
    graph = defaultdict(list)
    
    
    for _ in range(m):
        s, e = map_int()
        graph[s].append(e)
        graph[e].append(s)  
        
    
    one_edge = [i for i in range(1, n + 1) if len(graph[i]) == 1]
    two_edge = [i for i in range(1, n + 1) if len(graph[i]) == 2]
    more_edge = [i for i in range(1, n + 1) if len(graph[i]) > 2]
    
    if len(one_edge) == 2 and len(two_edge) == n - 2 and len(more_edge) == 0:
        print('bus topology')
    elif len(one_edge) == 0 and len(two_edge) == n and len(more_edge) == 0:
        print('ring topology')
    elif len(one_edge) == n -1 and len(two_edge) == 0 and len(more_edge) == 1:
        print('star topology')
    else:
        print('unknown topology')



def main():
    solve()

if __name__ == "__main__":
    main()