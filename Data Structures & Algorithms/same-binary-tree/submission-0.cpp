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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<pair<TreeNode*,TreeNode*>> frontier;  
        frontier.push({p,q});            
        while (frontier.size() > 0){
            pair<TreeNode*,TreeNode*> fr = frontier.front();
            frontier.pop();
            if (fr.first == nullptr && fr.second == nullptr) {
                continue;
            }
            if (fr.first == nullptr || fr.second == nullptr){return false;}
            if (fr.first->val != fr.second -> val){
                return false;
            }
            
            frontier.push({fr.first->left,fr.second->left});
            frontier.push({fr.first->right,fr.second->right});

        }
        return true;

    }
};
