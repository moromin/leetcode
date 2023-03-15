# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        hasNull = False
        q = collections.deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if hasNull:
                        return False
                    hasNull = False
                    q.append(node.left)
                    q.append(node.right)
                else:
                    hasNull = True
            # print(q, hasNull)
        return True