# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self,root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif (key > root.val):
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.findMin(root.right)
            if temp:
                temp.val,root.val =root.val,temp.val
                root.right = self.deleteNode(root.right, temp.val)
            else:
                root.right = None
        return root
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
