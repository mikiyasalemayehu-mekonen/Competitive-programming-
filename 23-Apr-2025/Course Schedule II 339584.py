# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*numCourses

        for u,v in  prerequisites:
            adj[v].append(u)
            indegree[u] = indegree[u] + 1

        
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for child in adj[c]:
                indegree[child] = indegree[child] - 1
                if indegree[child]==0:
                    queue.append(child)
        if len(res)!=numCourses:
            return []
        return res
