# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

n  , q = map(int,input().split())
prefix = [0]*(n+1)
for i in range(1,n+1):
    c,t = map(int,input().split())
    prefix[i] = prefix[i-1] + (c*t)
prefix = prefix[1:]
queries = list(map(int,input().split()))

index = 0
for qr in queries:
    while index<n:
        if qr<=prefix[index]:
            print(index+1)
            break
        index = index + 1
