# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = 0
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node, sums):
            if not node:
                return
            
            sums = sums * 10 + node.val

            if not node.left and not node.right:
                self.total += sums
                return
            traverse(node.left, sums)
            traverse(node.right, sums)
        
        traverse(root, 0)
        return self.total