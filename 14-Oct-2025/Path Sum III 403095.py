# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0  # return 0 for empty tree
        
        res = []

        def iterate(node, val):
            if not node:
                return False
            val.append(node.val)
        
            if sum(val) == targetSum:
               
                res.append(1)
          
            iterate(node.left, val)
            iterate(node.right, val)
        
            val.pop()
            return

        def traverse(node):
            if not node:
                return
            iterate(node, [])
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return len(res)
