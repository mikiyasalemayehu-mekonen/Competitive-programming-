# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        pos_ans = [i for i in range(1,n+1)]
        adj = defaultdict(list)
        for u,v in trust:
            adj[u].append(v)
            if u in pos_ans:
                pos_ans.remove(u)
        if len(pos_ans)!=1:
            return -1
        for i in range(1,n+1):
            if i==pos_ans[0]:
                continue
            elif pos_ans[0] not in adj[i]:
                break
        else:
            return pos_ans[0]

        return -1