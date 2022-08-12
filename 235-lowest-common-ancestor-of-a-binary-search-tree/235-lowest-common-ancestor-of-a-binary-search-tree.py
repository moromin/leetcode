# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, parents):
        if node is None:
            return parents
        if node.left is not None:
            parents[node.left] = node
            self.traverse(node.left, parents)
        if node.right is not None:
            parents[node.right] = node
            self.traverse(node.right, parents)
        return parents
    
    def lowestCommonAncestor(self, root, p, q):
        parents = {root: None}
        parents = self.traverse(root, parents)
        
        ancestors = set()
        parent = p
        
        while parent is not None:
            ancestors.add(parent)
            parent = parents[parent]
        
        node = q
        while node not in ancestors:
            node = parents[node]
        
        return node