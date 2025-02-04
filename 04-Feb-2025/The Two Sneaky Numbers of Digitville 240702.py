# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        ans=[]
        for key,value in count.items() :
            if count[key]==2:
                ans.append(key)

        return ans