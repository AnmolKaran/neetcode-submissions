/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* og = new ListNode();
        ListNode* tail = og;

        
        while (true){
            int minIdx = -1;
            for (int i = 0; i < lists.size(); i +=1){
                if (lists[i] != nullptr && (minIdx == -1 ||lists[i]->val < lists[minIdx]->val)){
                    minIdx = i;
                }

            }
            if (minIdx == -1){break;}
            tail->next = lists[minIdx];
            tail = tail->next;
            lists[minIdx] = lists[minIdx]->next; 
        }
        return og->next;
    }
};
