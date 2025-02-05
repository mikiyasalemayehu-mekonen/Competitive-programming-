# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first="qwertyuiop"
        second="asdfghjkl"
        three="zxcvbnm"  
        res=[]
        for word in words:
            count1=0
            count2=0
            count3=0
            for j in range(len(word)):
                temp=word[j].lower()
                if temp not in first:
                    count1+=1
                if temp not in second:
                    count2+=1
                if temp not in three:
                    count3+=1
            if count1==0 or count2==0 or count3==0:
                res.append(word)
        return res



        