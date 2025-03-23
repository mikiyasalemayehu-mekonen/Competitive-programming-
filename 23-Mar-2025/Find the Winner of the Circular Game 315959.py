# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for i in range(1,n+1):
            queue.append(i)

        def remove(que,k):
            if len(que)==1:
                return que[0]
            t = 1
            while t <k:
                temp = que.popleft()
                que.append(temp)
                t = t + 1
            que.popleft()
            return remove(que,k)
          
        return remove(queue,k) 
        
        