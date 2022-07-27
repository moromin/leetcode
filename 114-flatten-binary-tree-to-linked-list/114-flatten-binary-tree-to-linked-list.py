# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        
        q = deque()
        
        def traverse(node):
            if node is None:
                return
            
            q.append(node)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        
        q.popleft()
        while q:
            node = q.popleft()
            root.right = node
            root.left = None
            root = root.right
            