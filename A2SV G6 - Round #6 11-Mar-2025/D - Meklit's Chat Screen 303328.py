# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque

n , k = map(int,input().split())
message =  list(map(int,input().split()))
queue = deque()
count = 0
seen = set()
for i in range(n):
    if queue and message[i] not in seen and len(queue)<k:
        queue.appendleft(message[i])
        count = count + 1
        seen.add(message[i])
    elif queue and message[i] not in seen and len(queue)==k:
        temp = queue.pop()
        queue.appendleft(message[i])
        seen.remove(temp)
        seen.add(message[i])
    elif not queue:
        queue.appendleft(message[i])
        count = count + 1
        seen.add(message[i])
print(count)
print(*queue)