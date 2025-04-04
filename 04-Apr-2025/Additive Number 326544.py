# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n<3:
            return False
        def backtrack(store,i):
            if (i==n and len(store)>=3) :
                num1 = int(store[-3])
                num2 =int(store[-2])
                num3 = int(store[-1])
                if num1+num2!=num3:
                    return
                return True
            if len(store)>=3:
                num1 = int(store[-3])
                num2 =int(store[-2])
                num3 = int(store[-1])
                if num1+num2!=num3:
                    return

            for j in range(i,n):
                temp = num[i:j+1]
                if len(temp) > 1 and temp[0] == '0':
                    break
                store.append(temp)
                is_true = backtrack(store,j+1)
                if is_true:
                    return True
                store.pop()
            return False

        return backtrack([],0)
        