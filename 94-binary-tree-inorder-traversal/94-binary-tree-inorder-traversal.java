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
    public void traverse(TreeNode node, List<Integer> list) {
        if (node == null) {
            return;
        }
        traverse(node.left, list);
        list.add(node.val);
        traverse(node.right, list);
    }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        var res = new ArrayList<Integer>();
        
        traverse(root, res);
        return res;
    }
}