# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBetween(root, l, r):
            if not root:
                return True
            if root.val <= l or root.val >= r:
                return False
            return isBetween(root.left, l, root.val) and isBetween(root.right, root.val, r)
        return isBetween(root, float("-inf"), float("inf"))

        
            
