# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, minVal):
            if not node:
                return 0
            goodVal = 1 if node.val >= minVal else 0
            minVal = max(minVal, node.val)
            return goodVal + traverse(node.left, minVal) + traverse(node.right, minVal)
        
        return traverse(root, root.val)
        