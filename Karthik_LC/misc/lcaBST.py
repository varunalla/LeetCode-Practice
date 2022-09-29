# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        current = root
        
        while current:
            
            if current.val < p.val and current.val < q.val:
                current = current.right
            
            elif current.val > p.val and current.val > q.val:
                current = current.left

            else: 
                return current
                
