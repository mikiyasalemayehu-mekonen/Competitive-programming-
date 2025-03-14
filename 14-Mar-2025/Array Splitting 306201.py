# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n , k= map(int,input().split())
stones = list(map(int,input().split()))
if k == n:  
    print(0)
    exit()

gaps = [stones[i] - stones[i - 1] for i in range(1, n)]
gaps.sort(reverse=True)
print(sum(gaps) - sum(gaps[:k - 1]))