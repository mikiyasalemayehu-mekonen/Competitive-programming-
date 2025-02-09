# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = { key:value for key,value in sorted(count.items(),key = lambda item: item[1],reverse=True)}
        frequent = list(count.keys())

        return frequent[:k]
        