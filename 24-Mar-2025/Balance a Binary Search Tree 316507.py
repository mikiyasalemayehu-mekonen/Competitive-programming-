# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorderTraversal(root):
            ans = []
            if root:
                ans.extend(inorderTraversal(root.left))
                ans.append(root.val)
                ans.extend(inorderTraversal(root.right))
            return ans
        ans = inorderTraversal(root)

        def helper(left, right):
            if left > right:
               return None
            mid = (left + right)//2
            left = helper(left, mid - 1)
            right = helper(mid + 1, right)
            return TreeNode(ans[mid], left, right)
        return helper(0, len(ans) - 1)
        