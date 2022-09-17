/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null)
            return null;
        
        Node itr = head, next;
        while (itr != null) {
            next = itr.next;
            
            Node copy = new Node(itr.val);
            itr.next = copy;
            copy.next = next;
            
            itr = next;
        }
        
        itr = head;
        while (itr != null) {
            if (itr.random != null) {
                itr.next.random = itr.random.next;
            }
            itr = itr.next.next;
        }
        
        itr = head;
        Node dummyHead = new Node(0);
        Node copyItr = dummyHead, copy;
        while (itr != null) {
            next = itr.next.next;
            
            copy = itr.next;
            copyItr.next = copy;
            copyItr = copyItr.next;
            
            itr.next = next;
            itr = itr.next;
        }
        
        return dummyHead.next;
    }
}