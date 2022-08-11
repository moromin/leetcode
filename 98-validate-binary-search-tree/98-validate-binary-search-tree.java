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
    public boolean isValidBST(TreeNode root) {
        return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    public boolean helper(TreeNode node, long min, long max) {
        if (node == null)
            return true;
        else if (min >= (long)node.val || (long)node.val >= max)
            return false;
        
        return helper(node.left, min, (long)node.val) && helper(node.right, (long)node.val, max);
            
    }
}