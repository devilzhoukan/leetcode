## 21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

```C++
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* result = nullptr;
        ListNode* p1 = l1;
        ListNode* p2 = l2;
        
        if (l1 == nullptr) {
            return l2;
        }
        if (l2 == nullptr) {
            return l1;
        }
        
        if (l1->val < l2->val) {
            result = p1;
            p1 = p1->next;
        }
        else {
            result = p2;
            p2 = p2->next;
        }
        
        ListNode* tail = result;
        tail->next = nullptr;
        
        while (p1 != nullptr && p2 != nullptr) {
            if (p1->val < p2->val) {
                tail->next = p1;
                p1 = p1->next;
                tail = tail->next;
                tail->next = nullptr;
            }
            else {
                tail->next = p2;
                p2 = p2->next;
                tail = tail->next;
                tail->next = nullptr;
            }
        }
        
        if (p1 != nullptr) {
            tail->next = p1;
        }
        else {
            tail->next = p2;
        }
        return result;
    }
};
```

When I was writing, I was thinking about Merge K sorted Lists,
that will be much harder. See ya there.
