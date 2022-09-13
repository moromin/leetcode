/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */


class Solution {
    int max = 0;
    
    int traverse(TreeNode node) {
        if (node == null)
            return 0;
        
        int left = traverse(node.left);
        int right = traverse(node.right);
        
        max = Math.max(max, left + right);
        
        return Math.max(left, right) + 1;
    }
    
    public int diameterOfBinaryTree(TreeNode root) {
        traverse(root);
        return max;
    }
}