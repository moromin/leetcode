# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d = defaultdict(list)
        
        def search(node):
            if not node:
                return
            
            if node.left:
                d[node.val].append(node.left.val)
                d[node.left.val].append(node.val)
            if node.right:
                d[node.val].append(node.right.val)
                d[node.right.val].append(node.val)
            search(node.left)
            search(node.right)
            
        search(root)
        bfs = [target.val]
        seen = set(bfs)
        
        for i in range(k):
            new_level = []
            for val in bfs:
                for node_val in d[val]:
                    if node_val not in seen:
                        new_level.append(node_val)
            bfs = new_level
            seen |= set(bfs)
        return bfs
            