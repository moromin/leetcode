# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        
        slow = head
        fast = head.next.next
        
        while slow != fast:
            if not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            
            if not slow or not fast:
                return False
        
        return True
        