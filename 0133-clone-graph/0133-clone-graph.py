"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        
        def clone(head):
            if head.val in seen:
                return seen[head.val]
            
            res = Node(head.val, [])
            seen[head.val] = res
            for n in head.neighbors:
                res.neighbors.append(clone(n))
            return res
        
        return clone(node) if node else None 
        
        
        