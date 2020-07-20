## 23.Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

I know Divide and Conquer is the best solution with minimun space, but its code is not clear, I prefer priorityqueue

```Java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        class ListNodeComparator implements Comparator<ListNode> {
            public int compare(ListNode o1, ListNode o2) {
                return o1.val - o2.val;
            }
        }
        
        Queue<ListNode> q = new PriorityQueue<>(new ListNodeComparator());
        for (ListNode listNode: lists) {
            if (listNode != null) {
                q.add(listNode);
            }
        }
        
        ListNode head = new ListNode(0);
        ListNode current = head;
        
        while (!q.isEmpty()) {
            current.next = q.poll();
            current = current.next;
            ListNode next = current.next;
            if (next != null) {
                q.add(next);
            }
        }
        
        return head.next;
    }
}
```
How to use java priority. Google it or go to 
[https://www.liaoxuefeng.com/wiki/1252599548343744/1265120632401152](https://www.liaoxuefeng.com/wiki/1252599548343744/1265120632401152)

I perfer implements than @Override style.
