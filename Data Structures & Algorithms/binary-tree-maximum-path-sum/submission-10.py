# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def _max_path_sum(root):
            nonlocal res
            if not root:
                return 0
            left_max = _max_path_sum(root.left)
            right_max = _max_path_sum(root.right)
            res = max(res, left_max + right_max + root.val, left_max + root.val, right_max + root.val, root.val)
            return max(left_max+ root.val, right_max + root.val, root.val)
        _max_path_sum(root)
        return res