"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
#     queue
#     def levelOrder(self, root: 'Node') -> List[List[int]]:
#         if not root:
#             return []
        
#         res = []
#         q = collections.deque()
#         q.append(root)
#         while q:
#             tmp = []
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node:
#                     tmp.append(node.val)
#                     for child in node.children:
#                         q.append(child)
#             if tmp:
#                 res.append(tmp)
#         return res

    # recursion
    def levelOrder(self, root):
        if not root:
            return []
        
        res = []
        
        def bfs(nodes):
            if not nodes:
                return
            
            children, nexts = [], []
            for node in nodes:
                children.append(node.val)
                nexts += node.children
            res.append(children)
            bfs(nexts)
        
        bfs([root])
        return res
    
            
        
        