# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        freq = sorted(count.values(), reverse=True)
        length = len(arr)//2
        if freq[0]>=length:
            return 1
        for i in range(1,len(freq)):
            freq[i] = freq[i-1] + freq[i]
            if freq[i]>=length:
                return i+1


        