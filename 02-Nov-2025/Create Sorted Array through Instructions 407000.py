# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = len(instructions)
        ans = {i: [0, 0] for i in range(n)}

        def merge(left, right):
            i, j = len(left) - 1, len(right) - 1
            while i >= 0 and j >= 0:
                if instructions[left[i]] <= instructions[right[j]]:
                    ans[right[j]][1] += (len(left) - 1 - i)
                    j -= 1
                else:
                    i -= 1
 
            while j >= 0:
                ans[right[j]][1] += len(left)
                j -= 1

            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if instructions[left[i]] < instructions[right[j]]:
                    result.append(left[i])
                    i += 1
                else:
                    ans[right[j]][0] += i
                    result.append(right[j])
                    j += 1

            while j < len(right):
                ans[right[j]][0] += i
                result.append(right[j])
                j += 1

            result.extend(left[i:])
            return result

        def mergesort(l, r, arr):
            if l == r:
                return [arr[r]]
            mid = (l + r) // 2
            left = mergesort(l, mid, arr)
            right = mergesort(mid + 1, r, arr)
            return merge(left, right)

        mergesort(0, n - 1, list(range(n)))

       
        res = sum(min(ans[i]) for i in ans) % ((10 ** 9) + 7)
        return res
