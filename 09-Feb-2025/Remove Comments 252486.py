# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        main_code = []
        stack = []
        in_block = False
        temp = []
        for i in range(len(source)):
            j = 0
           
            while j < len(source[i]):
                if in_block:
                    if j + 1 < len(source[i]) and source[i][j:j+2] == "*/":
                        in_block = False
                        j += 1 
                else:
                    if j + 1 < len(source[i]) and source[i][j:j+2] == "//":
                        break 

                    elif j + 1 < len(source[i]) and source[i][j:j+2] == "/*":
                        in_block = True
                        j += 1  
                    else:
                        temp.append(source[i][j])
                j += 1
            if temp and not in_block:
                main_code.append("".join(temp))
                temp = []
        return main_code
  
        



  