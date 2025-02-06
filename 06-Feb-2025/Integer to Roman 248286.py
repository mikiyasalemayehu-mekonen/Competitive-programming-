# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        # symbols={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        # num_string=str(num)
        roman=[]
        while num>0:
            if num>=1000:
                roman.append("M") 
                num=num-1000
            elif num>=900:
                roman.append("CM") 
                num=num-900
            elif num>=500 :
                roman.append("D") 
                num=num-500
            elif num>=400 :
                roman.append("CD") 
                num=num-400
            elif num>=100:
                roman.append("C") 
                num=num-100
            elif num>=90:
                roman.append("XC") 
                num=num-90
            elif num>=50:
                roman.append("L") 
                num=num-50
            elif num>=40:
                roman.append("XL") 
                num=num-40
            elif num>=10:
                roman.append("X") 
                num=num-10
            elif num>=9:
                roman.append("IX") 
                num=num-9
            elif num>=5 :
                roman.append("V") 
                num=num-5
            elif num>=4 :
                roman.append("IV") 
                num=num-4
            else:
                roman.append("I") 
                num=num-1


        return "".join(roman)