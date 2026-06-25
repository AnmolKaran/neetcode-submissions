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
    bool isValidBST(TreeNode* root) {
        return helper(root,LONG_MIN, LONG_MAX);
    }

private:
    bool helper(TreeNode* root, long minRange, long maxRange){
        if (!root){
            return  true;
        }
        if (root->val <= minRange || root->val >= maxRange){
            return false;
        }
        bool rightResult = helper(root->right,root->val,maxRange);
        bool leftResult = helper(root->left,minRange,root->val);

        return rightResult && leftResult;
        
    }
};
