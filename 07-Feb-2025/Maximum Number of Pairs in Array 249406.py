# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        count_pairs = 0
        count_leftover = 0
        for value in count.values():
            if value%2==0:
                count_pairs+=value//2
            else:
                count_leftover += 1
                count_pairs+=(value-1)//2
        return [count_pairs,count_leftover]


