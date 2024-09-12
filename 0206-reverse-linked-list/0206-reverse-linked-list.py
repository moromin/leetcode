# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        next = head.next
        previous = None
        while next:
            next = head.next
            head.next = previous
            previous = head
            if next:
                head = next
        
        return head
        
            