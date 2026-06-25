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
    vector<int> rightSideView(TreeNode* root) {
        queue<pair<TreeNode*,int>> frontier;
        if (!root){
            return {};
        }
        vector<int> fin;
        frontier.push({root,0});
        while (frontier.size()>0){
            pair<TreeNode*,int> popped = frontier.front();
            frontier.pop();

            if (popped.second != frontier.front().second){
                fin.push_back(popped.first->val);
            }

            if (popped.first->left){
                frontier.push({popped.first->left, popped.second + 1});
            }
            if (popped.first->right){
                frontier.push({popped.first->right,popped.second+1});
            }

        }
        return fin;
    }
};
