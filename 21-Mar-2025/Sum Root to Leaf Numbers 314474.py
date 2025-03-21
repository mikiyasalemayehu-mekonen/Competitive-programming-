# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sums = 0
        def track(root,store):
            nonlocal sums
            store.append(str(root.val))
            if root.left:
                track(root.left,store)
            if root.right:
                 track(root.right,store)
            if not root.left and not root.right:
                sums = sums + int("".join(store))
            store.pop() 
        track(root,[])
        return sums