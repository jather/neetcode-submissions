# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, root.val)]
        while stack:
            node = stack.pop()
            largest = node[1]
            if node[0].val >= largest:
                res += 1
                largest = node[0].val
            if node[0].left:
                stack.append((node[0].left, largest))
            if node[0].right:
                stack.append((node[0].right, largest))
            
        return res


        