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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root){
            return false;
        }
        if (!subRoot){
            return true;
            
        }
        
        queue<TreeNode*> frontier;  
        frontier.push(root);
        while (frontier.size() > 0){
            
            TreeNode* fr = frontier.front();
            frontier.pop();
            if (!fr){
                continue;
            }
            
            if (fr->val == subRoot->val){
                bool isIt = isSameTree(fr,subRoot);
                if (isIt){
                    return true;
                }
            }
            frontier.push(fr->left);
            frontier.push(fr->right);

            
            
        }
        return false;
    }
private: 
    bool isSameTree(TreeNode* p, TreeNode* q) {
            // if(!p && !q){
            //     return true;
            // } else if (!p || !q){
            //     return false;
            // }
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
