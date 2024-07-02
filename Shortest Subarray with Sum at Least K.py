class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque()
        prefix_sum = [0] * (len(nums) + 1)
        min_length = len(nums) + 1
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        for i in range(len(prefix_sum)):
            while q and prefix_sum[i]-prefix_sum[q[0]]>=k :
                min_length=min(min_length,i-q.popleft())
            while q and prefix_sum[i] <= prefix_sum[q[-1]]:
                q.pop()
            q.append(i)
        return  min_length if min_length <= len(nums) else -1
