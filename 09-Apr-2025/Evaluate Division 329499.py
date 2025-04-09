# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        arr= defaultdict(list)
        i=0
        for u,v in equations:
            arr[u].append((v,values[i]))
            arr[v].append((u,1/values[i]))
            i+=1
        ans = []
        visited=set()
   
        def dfs(u,v,visited,value):
            print(u)
            if u==v:
                return value
            visited.add(u)
            for nieghours,val in arr[u]:
                if nieghours  not in visited:
                    # print(neighbours)
                    temp = dfs(nieghours ,v,visited,value*val)
                    if temp!=-1:
                        return temp
            return -1
        for u,v in queries:
            if u not in arr or v not in arr:
                ans.append(-1.00000)
            elif  u==v:
                ans.append(1.00000)
            else:
                temp = dfs(u,v,visited,1) 
                ans.append(temp)
            visited.clear()
        return ans