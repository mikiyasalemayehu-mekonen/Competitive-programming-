# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = deque((range(len(deck))))
        ans = [0]*len(deck)
        for n in deck:
            i = dq.popleft()
            ans[i] = n
            if dq:
                dq.append(dq.popleft()) 
        return ans