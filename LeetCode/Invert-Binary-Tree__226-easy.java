/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null){
            return null;
        }
        
        TreeNode righttemp = root.right;
        TreeNode left = root.left;
        
        root.right = left;
        root.left = righttemp;
        invertTree(root.left);
        invertTree(root.right);
        return root;
   
    }
}