# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q  = deque([root])
        while q:
            row_max = q[0].val
            n = len(q)
            for i in range(n):
                temp = q.popleft()
                row_max = max(row_max,temp.val) 
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            result.append(row_max)

        return result



        
