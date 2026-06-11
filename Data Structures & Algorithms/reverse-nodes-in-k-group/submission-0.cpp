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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* og = new ListNode();
        og->next = head;
        ListNode* prevGroup = og;

        while(true){
            ListNode* kth =prevGroup;
            for (int i = 0; i < k && kth != nullptr; i +=1){
                kth = kth ->next;
            }
            if (kth == nullptr){break;}

            ListNode* groupNext = kth->next;
            ListNode* prev = groupNext;
            ListNode* curr = prevGroup->next;
            while (curr != groupNext) {
                ListNode* nxt = curr->next;
                curr->next = prev;
                prev = curr;
                curr = nxt;
            }
            

            ListNode* newPrevGroup = prevGroup->next;
            prevGroup->next = kth;
            prevGroup = newPrevGroup;
        }
        return og->next;
    }
};
