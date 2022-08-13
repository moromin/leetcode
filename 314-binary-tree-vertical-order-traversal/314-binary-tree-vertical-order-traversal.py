# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = collections.defaultdict(list)
        q = [(root, 0)]
        for node, i in q:
            if node:
                cols[i].append(node.val)
                q += (node.left, i - 1), (node.right, i + 1)
        
        return [cols[i] for i in sorted(cols)]