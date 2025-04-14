# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        val = root.val
        while queue:
            temp = queue.popleft()
            if temp.val!=val:
                return False
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            
        return True

        