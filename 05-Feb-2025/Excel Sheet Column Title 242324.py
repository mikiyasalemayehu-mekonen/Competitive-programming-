# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column_title=[]
        length=1
        while columnNumber>0:
            temp=columnNumber%26
            if temp==0:
                column_title.append("Z")
                columnNumber-=1
            else:
                column_title.append(chr(ord("A")+temp-1))
            columnNumber=int(columnNumber/26)
        column_title.reverse()
        return "".join(column_title)


        