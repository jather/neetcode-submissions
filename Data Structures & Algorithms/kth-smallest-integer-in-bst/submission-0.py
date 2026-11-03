# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 1
    res = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderDFS(root):
            if root.left:
                inorderDFS(root.left)
            if self.count == k:
                self.res = root.val
            self.count += 1
            if root.right:
                inorderDFS(root.right)
        inorderDFS(root)
        return self.res