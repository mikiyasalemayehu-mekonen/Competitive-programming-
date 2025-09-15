# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length =  len(temperatures)
        stack =[ ]
        res = {i:0 for i in range(length) }
        for i in range(length):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                tem = stack.pop()
                res[tem] = i-tem
            stack.append(i)
        return [v for v in res.values()]