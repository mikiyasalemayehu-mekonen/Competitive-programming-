# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        balls = list(map(int,s))
        ptr1 = 0
        count =  0
        for ptr2 in range(len(balls)):
            if balls[ptr1] == 0 :
                ptr1 = ptr1 + 1
                continue
            if balls[ptr2] ==0:
                balls[ptr1] , balls[ptr2] = balls[ptr2] , balls[ptr1]
                count = count + ptr2-ptr1
                ptr1 = ptr1 + 1

        return count 
    
        