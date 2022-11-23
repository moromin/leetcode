# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lenMax = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            self.lenMax = max(self.lenMax, left + right)
            return max(left, right) + 1
        
        traverse(root)
        return self.lenMax
            