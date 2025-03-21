# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s) 
        def backtrack(i,store):
            if i==n:
                if len(store) ==1:
                    return False
                return True 
            for j in range(i+1,n+1):
                if not store or int(store[-1]) == int(s[i:j])+1:
                    store.append(s[i:j])
                    check = backtrack(j,store)
                    store.pop()
                    if check:
                        return True
            return False
                
        return backtrack(0,[])


                            