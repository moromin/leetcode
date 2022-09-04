# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        
        def traverse(node, row, col):
            if not node:
                return
            d[col].append((row, node.val))
            traverse(node.left, row+1, col-1)
            traverse(node.right, row+1, col+1)
        
        traverse(root, 0, 0)
        
        res = []
        for i in sorted(d.keys()):
            tmp = []
            for elem in sorted(d[i]):
                tmp.append(elem[1])
            res.append(tmp)
        return res