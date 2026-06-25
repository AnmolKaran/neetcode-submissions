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
private:
    int globalMax = INT_MIN;


    int dfs(TreeNode*root){
        if (!root){
            return 0;
        }
        int singlePathMax = 0;
        int lft = max(0,dfs(root -> left));
        int rt = max(0,dfs(root->right));
        if (max({lft,rt,lft + rt + root->val}) > globalMax){
            globalMax = max(globalMax,lft + rt + root->val);
        }

        singlePathMax = max(root->val + lft, root->val + rt);
        return singlePathMax;
    }


public:

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return globalMax;
    }
};
