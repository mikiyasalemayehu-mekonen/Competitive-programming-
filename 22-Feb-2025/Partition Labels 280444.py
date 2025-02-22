# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        
        char = s[0]
        length = []
        left = 0
        for i in range(len(s)):
            if s[i]!=char and last[s[i]]>last[char]:
                char = s[i]

            if s[i] ==char and last[char]==i:
                length.append(i-left+1)
                if i+1<len(s):
                    char = s[i+1]
                    left = i + 1
        return length


        
                


        