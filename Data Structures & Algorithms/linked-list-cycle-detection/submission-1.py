# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return False
        s, f = head, head.next
        while s is not f:
            s = s.next
            if f.next is None:
                return False
            f = f.next
            if f.next is None:
                return False
            f = f.next
        return True 
                
        