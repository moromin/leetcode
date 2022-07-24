# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = node1 = ListNode()
        head2 = node2 = ListNode()
        
        while head:
            if head.val < x:
                node1.next = head
                node1 = node1.next
            else:
                node2.next = head
                node2 = node2.next
            head = head.next
        
        node1.next = head2.next
        node2.next = None
        return head1.next
            
        