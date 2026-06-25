/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int goodNodes(TreeNode* root) {
        if (!root){
            return 0;
        }
        return 1 + helperGoodNodes(root->left,root->val) + helperGoodNodes(root->right,root->val);
    }
private:
    int helperGoodNodes(TreeNode* root,int  max_so_far){
        if (!root){
            return 0;
        }
        if (root->val >= max_so_far){
            return 1 + helperGoodNodes(root->left,root->val) + helperGoodNodes(root->right,root->val);
        }
        else {
            return  helperGoodNodes(root->left,max_so_far) + helperGoodNodes(root->right,max_so_far);
        }


    }
};
