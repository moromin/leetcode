# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diff = 0
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, Min, Max):
            if not node:
                return
            Min = min(Min, node.val)
            Max = max(Max, node.val)
            self.diff = max(self.diff, abs(Max - Min))
            traverse(node.left, Min, Max)
            traverse(node.right, Min, Max)
        
        traverse(root, root.val, root.val)
        return self.diff