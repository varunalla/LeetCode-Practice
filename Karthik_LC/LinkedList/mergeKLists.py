# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        while len(lists) > 1:
            
            mergedLists = []
            
            for i in range(0, len(lists) , 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                
                mergedLists.append(self.mergeTwoLists(list1, list2))
            
            lists = mergedLists
        
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        
        dummy = ListNode()
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            
            cur = cur.next
            
        if l1:
                cur.next = l1
        if l2:
                cur.next = l2
            
        return dummy.next
            
            
