# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = collections.defaultdict(list)
        
        def traverse(node, depth):
            if not node:
                return
            d[depth].append(node.val)
            traverse(node.right, depth+1)
            traverse(node.left, depth+1)
        
        traverse(root, 0)
        
        return [sum(d[k]) / len(d[k]) for k in d.keys()]