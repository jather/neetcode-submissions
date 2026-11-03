# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        if not list1:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        if not list2:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        elif list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(list1, list2))
            lists = mergedLists
        return lists[0]


        