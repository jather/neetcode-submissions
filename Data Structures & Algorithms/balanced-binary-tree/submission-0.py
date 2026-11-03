# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isBalancedB = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            self.findDepth(root)
            return self.isBalancedB
    def findDepth(self, root):
        if not root.left and not root.right:
            return 1
        leftDepth, rightDepth = 0, 0
        if root.left:
            leftDepth = self.findDepth(root.left) 
        if root.right: 
            rightDepth = self.findDepth(root.right) 
        if abs(leftDepth - rightDepth) > 1:
            self.isBalancedB= False
        return max(leftDepth, rightDepth) + 1