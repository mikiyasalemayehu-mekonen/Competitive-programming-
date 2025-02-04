# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        masked=''
        if '@' in s:
            s=s.lower()
            name , domain = s.split('@')
            print
            if len(name)>1:
                masked=name[0]+"*****"+name[-1]+'@'+domain
            else:
                masked=name[0]+"*****"+'@'+domain
            return masked
        else:
            for char in s:
                if  not char.isalnum():
                    s=s.replace(char,"")
            masked="***-***-"+s[-4:]
            length=len(s)
            if length>10:
                masked="-"+masked
                for i in range(length-10):
                    masked="*"+masked
                masked="+"+masked

            return masked


        