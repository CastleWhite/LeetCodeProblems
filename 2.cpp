/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int prev_l = 0;
        ListNode *head = new ListNode(0);
        ListNode *l3 = head;
        while (l1!=NULL && l2!=NULL)
        {
            int l = l1->val+l2->val+prev_l;
            if (l>9)
            {
                prev_l = 1;
                l -= 10;
            }
            else 
            {
                prev_l = 0;
            }
            ListNode *l3_next = new ListNode(l);
            l3->next = l3_next;
            l3 = l3_next;
            l1 = l1->next;
            l2 = l2->next;
            
        }
        ListNode *ll = (l1==NULL)?l2:l1;
             
        while (ll!=NULL)
        {
            int l = ll->val+prev_l;
            if (l>9)
            {
                prev_l = 1;
                l -= 10;
            }
            else 
            {
                prev_l = 0;
            }
            ListNode *l3_next = new ListNode(l);
            l3->next = l3_next;
            l3 = l3_next;
            ll = ll->next;
            
        }
            
        if (prev_l != 0)
        {
            ListNode *l3_next = new ListNode(1);
            l3->next = l3_next;
        }
        return head->next;
    }
};
