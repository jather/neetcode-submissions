# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        target = length - n

        if target == 0:
            head = head.next
            return head

        cur = head
        for i in range(target):
            if i == target - 1:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head




            
