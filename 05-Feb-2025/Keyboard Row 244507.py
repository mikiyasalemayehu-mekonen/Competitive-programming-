# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first="qwertyuiop"
        second="asdfghjkl"
        there="zxcvbnm"
       
        res=[]
        for word in words:
            c_one=0
            c_two=0
            c_there=0
            for j in range(len(word)):
                temp=word[j].lower()
                if temp not in first:
                    c_one+=1
                if temp not in second:
                    c_two+=1
                if temp not in there:
                    c_there+=1
            if c_one==0 or c_two==0 or c_there==0:
                res.append(word)
        return res



        