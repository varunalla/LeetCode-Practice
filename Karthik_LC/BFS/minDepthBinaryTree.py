# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        levelQueue = deque()
        levelQueue.append(root)
        minDepth = 0
        
        while levelQueue:
            levelSize = len(levelQueue)
            minDepth += 1
            
            for _ in range(levelSize):
                curNode = levelQueue.popleft()
                
                
                if not curNode.left and not curNode.right:
                    return minDepth
                
                if curNode.left:
                    levelQueue.append(curNode.left)
                if curNode.right:
                    levelQueue.append(curNode.right)
                
            
                    
            
            
            
        
        
        
