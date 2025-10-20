# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent_val, grandparent_val):
            if not node:
                return 0
            current_sum = node.val if grandparent_val % 2 == 0 else 0
            left_sum = dfs(node.left, node.val, parent_val)
            right_sum = dfs(node.right, node.val, parent_val)
          
            
            return current_sum + left_sum + right_sum
        
        return dfs(root, 1, 1)