# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def iterate(root,val):
          
            if val-root.val==0 and (not  root.left and not root.right):
                return True
            d1,d2 = False,False
            if root.left:
                d1 = iterate(root.left,val-root.val)
            if root.right:
                d2 = iterate(root.right,val-root.val)
            return d1 or d2
        return iterate(root,targetSum)

        