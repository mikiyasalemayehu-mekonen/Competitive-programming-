# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack =[0]
        for i in range(1,len(temperatures)):
            if temperatures[stack[-1]] < temperatures[i]:
                ans[stack[-1]] = i-stack[-1]
                stack.pop()
                while stack and temperatures[stack[-1]] < temperatures[i]:   
                    ans[stack[-1]] = i-stack[-1]
                    stack.pop()
            stack.append(i)
        for i in range(len(temperatures)-len(ans)):

            ans.append(0)
        return ans


