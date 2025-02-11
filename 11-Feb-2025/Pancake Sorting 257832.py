# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for num in range(len(arr),1,-1):
            index = arr.index(num)
            if num==index+1:
                continue
            
            if index!=0:
                flips.append(index+1)
            flips.append(num)

            arr[:index+1] = reversed(arr[:index+1] )

            arr  = arr[num-1:0:-1] + [arr[0]] + arr[num:]

        return flips

        