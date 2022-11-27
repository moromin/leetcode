# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        map = defaultdict(list)
        
        def traverse(node, depth):
            if not node:
                return
            map[depth].append(node.val)
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)
        
        traverse(root, 0)
        for depth in map.keys():
            res.append(map[depth][-1])
        return res
    