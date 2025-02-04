# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_map={}
        for i in range(len(paths)):
            x=paths[i].split()
            for j in range(1,len(x)):
                temp=x[j]
                file_path=x[0]+"/"+temp[:temp.index("(")]
                path_map[temp[temp.index("("):]] = path_map.get(temp[temp.index("("):],[])
                path_map[temp[temp.index("("):]].extend([file_path])
        
        duplicates=[]
       
        return [ value for  value in path_map.values() if len(value)>=2]


        