# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def traverse(node):
            if not node.left and not node.right:
                return [node.val]
            res = []
            if node.left:
                res += traverse(node.left)
            if node.right:
                res += traverse(node.right)
            return res
        
        l1 = traverse(root1)
        l2 = traverse(root2)
        
        return l1 == l2