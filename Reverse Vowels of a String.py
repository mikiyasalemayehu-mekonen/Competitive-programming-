class Solution:
    def reverseVowels(self, s: str) -> str:
        seek=0
        hold=len(s)-1
        temp=list(s)
        while seek<=hold:
            if (temp[seek].lower()=="a" or  temp[seek].lower()=="e"  or  temp[seek].lower()=="i"  or  temp[seek].lower()=="o"  or  temp[seek].lower()=="u") and (temp[hold].lower()=="a" or  temp[hold].lower()=="e"  or  temp[hold].lower()=="i"  or  temp[hold].lower()=="o"  or  temp[hold].lower()=="u") :
                temp[hold],temp[seek]=temp[seek],temp[hold]
                hold-=1
                seek+=1
            elif (temp[seek].lower()=="a" or  temp[seek].lower()=="e"  or  temp[seek].lower()=="i"  or  temp[seek].lower()=="o"  or  temp[seek].lower()=="u") and (temp[hold].lower()!="a" or  temp[hold].lower()!="e"  or  temp[hold].lower()!="i"  or  temp[hold].lower()!="o"  or  temp[hold].lower()!="u"):
                hold-=1 
            elif  (temp[seek].lower()!="a" or  temp[seek].lower()!="e"  or  temp[seek].lower()!="i"  or  temp[seek].lower()!="o"  or  temp[seek].lower()!="u") and (temp[hold].lower()=="a" or  temp[hold].lower()=="e"  or  temp[hold].lower()=="i"  or  temp[hold].lower()=="o"  or  temp[hold].lower()=="u"):
                seek+=1 
            else:
                hold-=1
                seek+=1 
        s="".join(temp)
        return s
            
