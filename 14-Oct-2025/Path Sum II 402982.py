# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []  
        
        res = []

        def iterate(node, val):
            if not node:
                return False
            val.append(node.val)
        
            if not node.left and not node.right and sum(val) == targetSum:
                res.append(val[:])  
                val.pop()
                return True
            d1 = iterate(node.left, val) if node.left else False
            d2 = iterate(node.right, val) if node.right else False
        
            val.pop()
            
            return d1 or d2

        iterate(root, [])
        return res
