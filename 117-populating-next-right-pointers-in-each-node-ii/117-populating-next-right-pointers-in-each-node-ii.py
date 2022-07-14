"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            pre = None
            while n:
                node = q.popleft()
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n -= 1
            pre.next = None
        
        return root