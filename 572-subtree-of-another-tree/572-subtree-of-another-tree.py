# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkNode(origin, sub):
            if origin is None and sub is not None:
                return False
            elif origin is not None and sub is None:
                return False
            elif origin is None and sub is None:
                return True
            
            if origin.val != sub.val:
                return False
            
            return checkNode(origin.left, sub.left) and checkNode(origin.right, sub.right)
        
        q = deque()
        q.append(root)
        while len(q) > 0:
            node = q.popleft()
            if checkNode(node, subRoot):
                return True
            if node is None:
                continue
            q.append(node.left)
            q.append(node.right)
        return False
        
        
         
        