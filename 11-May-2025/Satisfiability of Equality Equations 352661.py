# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
       
        root = {char: char for char in string.ascii_lowercase}
        def get(x):
            if root[x]!=x:
                root[x] = get(root[x])
            return root[x]

        def union(x,y):
            pa_x = get(x)
            pa_y = get(y)
            if pa_x!=pa_y:
                root[pa_y] = pa_x
             
        for equ in equations:
            if equ[1]=="=":
                union(equ[0],equ[3])
        for equ in equations:
            if equ[1]=="!":
                tem1 = get(equ[0])
                tem2 = get(equ[3])
                if tem1==tem2:
                    return False
      
        return True