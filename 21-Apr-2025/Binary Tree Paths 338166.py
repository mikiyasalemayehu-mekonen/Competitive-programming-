# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return [str(root.val)]
        result = []
        def traverse(root,temp):
            nonlocal result
            if not root:
                result.append(temp)
                return
            temp = temp+"->"+str(root.val)
            if root.left:
                traverse(root.left,temp)
            if root.right:
                traverse(root.right,temp)
            if not root.left and not root.right:
                result.append(temp)
        if root.left:
                traverse(root.left,str(root.val))
        if root.right:
                 traverse(root.right,str(root.val))
        
        return result
