# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        res = []
        if root:
            nodes.append(root)
        while nodes:
            res.append(x.val for x in nodes)
            new_nodes = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            nodes = new_nodes
        return res



        
        