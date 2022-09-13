# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if root is None:
            return result
        
        levelQueue = deque()
        levelQueue.append(root)
        
        while levelQueue:
            levelSize = len(levelQueue)
            curLevel = []
            
            for _ in range(levelSize):
                curNode = levelQueue.popleft()
                curLevel.append(curNode.val)
                
                
                if curNode.left:
                    levelQueue.append(curNode.left)
                if curNode.right:
                    levelQueue.append(curNode.right)
            
            #Only difference from regular level order traversal is, instead of                  
            #appending the elements at the end of the result list, we insert each                 
            #level elements at the beginning.
            
            result.insert(0, curLevel)
        
        return result
        
