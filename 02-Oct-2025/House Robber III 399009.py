# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right                                       
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(root):
            if not root:
                return 0
            include,exclude = root.val,0
            if root in memo:
                return memo[root]
            if root.left:
                include = root.val + dp(root.left.left) + dp(root.left.right)
                exclude =  dp(root.left)
            if root.right:
                include = include + dp(root.right.left) + dp(root.right.right)
                exclude =  exclude + dp(root.right)
            memo[root] = max(include,exclude)

            return memo[root]
        
        return dp(root)
