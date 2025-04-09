# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        pos_ans = set([i for i in range(1,n+1)])
        adj = defaultdict(list)
        for u,v in trust:
            adj[u].append(v)
            if u in pos_ans:
                pos_ans.remove(u)
        if len(pos_ans)!=1:
            return -1
        val = pos_ans.pop()
        for i in range(1,n+1):
            if i==val:
                continue
            elif val not in adj[i]:
                break
        else:
            return val

        return -1