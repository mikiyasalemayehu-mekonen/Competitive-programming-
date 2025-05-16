# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = ("a","e","i","o","u")
        prefix =[0]*(len(s))
        for i in range(len(s)):
            if s[i] in vowels:
                prefix[i] = prefix[i-1] ^ ord(s[i])
            else:
                prefix[i] = prefix[i-1] 
        prefix = [0] + prefix
        
        ranges = defaultdict(list)
        for i in range(len(prefix)):
            ranges[prefix[i]].append(i)

        maximum = 0
        for r in ranges:
            if len(ranges[r])>=2:
                tem = (ranges[r][-1]-ranges[r][0]) 
                maximum = max(maximum,tem)
        return maximum


        
        

        