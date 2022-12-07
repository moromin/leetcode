# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sums = 0
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def traverse(node):
            if not node:
                return
            if low <= node.val <= high:
                self.sums += node.val
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return self.sums
        