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
        node_list = {}
        cur = head
        dummy = Node(0)
        copy_cur = dummy
        while cur:
            copy_cur.next = Node(cur.val)
            copy_cur = copy_cur.next
            node_list[cur] = copy_cur
            cur = cur.next
        
        cur = head
        copy_cur = dummy
        while cur:
            random_pointer = None if not cur.random else node_list[cur.random]
            copy_cur = copy_cur.next
            copy_cur.random = random_pointer
            cur = cur.next
        return dummy.next
         
        