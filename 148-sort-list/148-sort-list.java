/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private ListNode merge(ListNode n1, ListNode n2) {
        ListNode dummyHead = new ListNode(0);
        ListNode iter = dummyHead;
        
        while (n1 != null && n2 != null) {
            if (n1.val < n2.val) {
                iter.next = n1;
                n1 = n1.next;
            } else {
                iter.next = n2;
                n2 = n2.next;
            }
            iter = iter.next;
        }
        if (n1 != null)
            iter.next = n1;
        if (n2 != null)
            iter.next = n2;
        return dummyHead.next;
    }
    
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        
        ListNode prev = null, slow = head, fast = head;
        
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        prev.next = null;
        
        ListNode n1 = sortList(head);
        ListNode n2 = sortList(slow);

        return merge(n1, n2); 
    }
}