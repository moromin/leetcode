# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(node, pre):
            if not node:
                return 0
            
            pre = max(node.val, pre)
            res = traverse(node.left, pre) + traverse(node.right, pre)
            return res if pre > node.val else res + 1
        
        return traverse(root, -math.inf) 