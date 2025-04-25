# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for u,v in  prerequisites:
            graph[v].append(u)
            indegree[u] = indegree[u] + 1
        
        queue = deque()
        ans =[]
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
                ans.append(i)
        
        while queue:
            temp = queue.popleft()
            for u in graph[temp]:
                indegree[u] = indegree[u] - 1
                if indegree[u]==0:
                    ans.append(u)
                    queue.append(u)
        return ans if len(ans)==numCourses else []
        
        
   
