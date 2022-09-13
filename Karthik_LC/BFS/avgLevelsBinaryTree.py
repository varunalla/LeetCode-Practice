# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        
        if root is None:
            return result
        
        levelQueue = deque()
        levelQueue.append(root)
        
        while levelQueue:
            levelSize = len(levelQueue)
            levelSum = 0.0
            
            for _ in range(levelSize):
                curNode = levelQueue.popleft()
                
                levelSum += curNode.val
                
                if(curNode.left):
                    levelQueue.append(curNode.left)
                if(curNode.right):
                    levelQueue.append(curNode.right)
                
            result.append(levelSum/levelSize)
        
        return result
        
