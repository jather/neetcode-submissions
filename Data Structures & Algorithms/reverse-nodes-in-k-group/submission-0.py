# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next:
            prev_tail = cur
            old_head = cur.next
            for _ in range(k):
                if not cur.next:
                    print(cur.val)
                    print("leftover")
                    return dummy.next
                cur = cur.next
            #move pointer to end of section
            next_head = cur.next
            cur.next = None
            #save next head, and unlink
            reversed_list = self.reverseList(old_head)
            #reverse current section. reversed_list is new head
            old_head.next = next_head
            prev_tail.next = reversed_list
            cur = old_head


        return dummy.next

                



        