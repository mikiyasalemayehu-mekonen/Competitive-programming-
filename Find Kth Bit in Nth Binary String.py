class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def find_kth(n, k):
            if n == 1:
                return '0'
            
            length = (1 << n) - 1  
            mid = (length // 2) + 1 

            if k == mid:
                return '1'
            elif k < mid:
                return find_kth(n - 1, k)
            else:
                mirrored_k = length - k + 1

                return '0' if find_kth(n - 1, mirrored_k) == '1' else '1'
        
        return find_kth(n, k)
