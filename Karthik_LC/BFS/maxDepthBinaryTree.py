# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        leftDepth = 1 + self.maxDepth(root.left)
        rightDepth = 1 + self.maxDepth(root.right)
        
        return max(leftDepth, rightDepth)
