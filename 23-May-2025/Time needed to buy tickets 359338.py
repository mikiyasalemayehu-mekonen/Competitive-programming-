# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque((i, t) for i, t in enumerate(tickets))
        time = 0

        while queue:
            i, t = queue.popleft()
            t -= 1
            time += 1

            if t > 0:
                queue.append((i, t))
            if i == k and t == 0:
                return time  
