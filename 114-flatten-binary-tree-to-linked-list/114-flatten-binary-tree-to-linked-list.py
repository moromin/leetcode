# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    pre = None
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.pre
        root.left = None
        self.pre = root
            