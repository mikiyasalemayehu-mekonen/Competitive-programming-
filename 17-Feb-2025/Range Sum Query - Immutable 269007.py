# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.lists = nums
        for i in range(1,len(self.lists)):
            self.lists[i] = self.lists[i-1] + self.lists[i]
        

    def sumRange(self, left: int, right: int) -> int:
      
        if left == 0:
            return self.lists[right]
        else:
            return self.lists[right] -self.lists[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)