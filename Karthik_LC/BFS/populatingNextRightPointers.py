"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return root
        
        leftMost = root
        
        while leftMost.left:
            
            head = leftMost
            
            while head:
            
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftMost = leftMost.left

        return root
        
