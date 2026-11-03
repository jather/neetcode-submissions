# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow

        l1 = head
        l2 = mid.next
        mid.next = None
        nxt, prev = None, None
        curr = l2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        l2 = prev
        
        l1cur = l1
        l2cur = l2
        l1nxt, l2nxt = None, None
        while l2cur:
            l1nxt = l1cur.next
            l1cur.next = l2cur
            l1cur = l1nxt
            l2nxt = l2cur.next
            l2cur.next = l1cur
            l2cur = l2nxt







        