# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        maximum = 0
        left = 0
        right = 1
        count = set()
        count.add(s[left])

        while left<=right and right<len(s):
            print(count)
            while  right<len(s) and  s[right] not in count : 
                count.add(s[right])
                right = right + 1
                maximum = max(maximum,len(count))
            if right<len(s) and s[right]  in count :
                count.remove(s[left])
                left = left + 1
                # right = right + 1
            maximum = max(maximum,len(count))

        return maximum

        