# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks):
        n = len(tasks)
        tasks = sorted([(enq, proc, i) for i, (enq, proc) in enumerate(tasks)])
        result = []
        heap = []
        time = 0
        i = 0
        
        while i < n or heap:
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]
            while i < n and tasks[i][0] <= time:
                enq, proc, idx = tasks[i]
                heapq.heappush(heap, (proc, idx))
                i += 1
            

            if heap:
                proc, idx = heapq.heappop(heap)
                time += proc
                result.append(idx)
        
        return result
