# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val==val:
            return root
        elif root and root.val>val:
            return self.searchBST(root.left,val)
        elif root and root.val<val:
            return self.searchBST(root.right,val)
        else:
            return None