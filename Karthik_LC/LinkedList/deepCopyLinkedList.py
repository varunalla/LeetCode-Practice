"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        current = head
        deepCopyHash = {None : None}
        
        while current:
            copy = Node(current.val)
            deepCopyHash[current] = copy
            current = current.next
            
        current = head
        
        while current:
            copy = deepCopyHash[current]
            copy.next = deepCopyHash[current.next]
            copy.random = deepCopyHash[current.random]
            current = current.next
            
        
        return deepCopyHash[head]
        
