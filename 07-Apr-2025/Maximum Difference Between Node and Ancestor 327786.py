# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root,mini,maxi):
            if not root:
                return float("-inf")
            mini = min(mini,root.val)
            maxi = max(maxi,root.val)
            left = helper(root.left,mini,maxi)
            right = helper(root.right,mini,maxi)
            return max(maxi-mini,max(left,right))
        return helper(root,float("inf"),float("-inf"))
        