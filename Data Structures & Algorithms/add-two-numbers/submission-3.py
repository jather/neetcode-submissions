# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2        
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while p1 or p2:
            if not p1:
                total = p2.val + carry
                value = total % 10
                carry = total // 10
                cur.next = ListNode(value)
                cur = cur.next
                p2 = p2.next
            elif not p2:
                total = p1.val + carry
                value = total % 10
                carry = total // 10
                cur.next = ListNode(value)
                cur = cur.next
                p1 = p1.next
            else:
                total = p1.val + p2.val + carry
                value = total % 10
                carry = total // 10
                cur.next = ListNode(value)
                cur = cur.next
                p1 = p1.next
                p2 = p2.next

        if carry:
            cur.next = ListNode(1)

        return dummy.next
            





        