# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    cur = 0
    inorder_map = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_map = {node: index for index, node in enumerate(inorder)}
        def _build_tree(pre_l, pre_r, in_l, in_r):
            if pre_r - pre_l < 0 or in_r - in_l < 0:
                return None
            cur = preorder[pre_l]
            node = TreeNode(cur)
            mid = self.inorder_map[cur]
            node.left = _build_tree(pre_l + 1, pre_l + 1 + mid - in_l, in_l, mid - 1)
            node.right = _build_tree(pre_l + 1 + mid - in_l, pre_r, mid + 1, in_r)
            return node

        return _build_tree(0, len(preorder) - 1, 0, len(preorder) - 1)


        