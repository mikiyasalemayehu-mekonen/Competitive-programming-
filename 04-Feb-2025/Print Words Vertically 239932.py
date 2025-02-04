# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        vertical=[]
        temp = s.split()
        rows = max(len(word) for word  in temp)
        for i in range(rows):
            word=[]
            for j in range(len(temp)):
                t=temp[j]
                if len(t)-1>=i:
                    word.append(t[i])
                else:
                    word.append(" ")
            vertical.append("".join(word).rstrip())
        return vertical


        