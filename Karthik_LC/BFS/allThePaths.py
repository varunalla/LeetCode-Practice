# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSumHelper(self, node, remainingSum, currentPath, allThePaths):
        
        if not node:
            return 
        
        currentPath.append(node.val)
        
        if node.val == remainingSum and not node.left and not node.right:
            allThePaths.append(list(currentPath))
        
        else:
            self.pathSumHelper(node.left, remainingSum - node.val, currentPath, allThePaths)

            self.pathSumHelper(node.right, remainingSum - node.val, currentPath, allThePaths)

        currentPath.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        allThePaths = []
        self.pathSumHelper(root, targetSum, [], allThePaths)
        return allThePaths
    
