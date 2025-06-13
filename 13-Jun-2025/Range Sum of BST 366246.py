# Problem: Range Sum of BST - https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return
            if low<=root.val<=high:
                self.ans = self.ans + root.val
            if root.right and root.val<=high:
                dfs(root.right)
            if root.left and root.val>=low:
                dfs(root.left)
        dfs(root)
        return self.ans
        