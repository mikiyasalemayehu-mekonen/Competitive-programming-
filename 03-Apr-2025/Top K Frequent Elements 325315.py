# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_counter = Counter(nums)
        n = len(nums)
        my_buckets = [0]*(n+1) 
        for item, freq in my_counter.items():
            if my_buckets[freq] == 0:
                my_buckets[freq] = [item]
            else:
                my_buckets[freq].append(item)
        result = []
        for i in range(n, -1, -1):
            if len(result) != k and my_buckets[i] != 0:
                result.extend(my_buckets[i])  
        return result

                