# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) 
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        print(nums)
    def add(self, val: int) -> int:
        if self.nums and len(self.nums)>=self.k:
            temp =  heapq.heappop(self.nums)
            if temp>val:
                heapq.heappush(self.nums,temp)
                return temp
            else:
                heapq.heappush(self.nums,val)
                return self.nums[0]
        else:
            heapq.heappush(self.nums,val)
            return self.nums[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)