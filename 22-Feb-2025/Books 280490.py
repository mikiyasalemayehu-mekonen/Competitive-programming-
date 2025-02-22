# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
time = list(map(int, input().split()))

left = 0
current_time = 0
max_books = 0

for right in range(n):
    current_time += time[right]
    
    while current_time > t:
        current_time -= time[left]
        left += 1
    
    max_books = max(max_books, right - left + 1)

print(max_books)
