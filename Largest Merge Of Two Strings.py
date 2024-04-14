class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = []
        ptr1 = 0
        ptr2 = 0
        while ptr1<len(word1) and ptr2<len(word2):
            if word1[ptr1] > word2[ptr2]: 
                ans.append(word1[ptr1])
                ptr1+=1
            elif word2[ptr2] > word1[ptr1]:  
                ans.append(word2[ptr2])
                ptr2+=1
            else: 
                if word1[ptr1:] >= word2[ptr2:]:  
                    ans.append(word1[ptr1])
                    ptr1+=1
                else:
                    ans.append(word2[ptr2])
                    ptr2+=1
        ans += word1[ptr1:] + word2[ptr2:]
        return "".join(ans)
    
