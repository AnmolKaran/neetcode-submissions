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

class Codec {
private:
    TreeNode* buildTree(const string& data, int& i){
        if (i >= data.size()) return nullptr;

        string token = "";
        while (i< data.size() && data[i] != ' '){
            token += data[i];
            i++;
        }
        i++;
        if (token == "N") return nullptr;
        
        TreeNode* root = new TreeNode(stoi(token));
        root->left = buildTree(data,i);
        root->right = buildTree(data,i);
        return root;
        
    }
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root){ return "N";}

        string fin = to_string(root->val) +" " +  serialize(root->left) + " " + serialize(root -> right);
        //cout<< fin + "\n";
        return fin;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int k = 0;
        return buildTree(data,k);
    }

    
};
