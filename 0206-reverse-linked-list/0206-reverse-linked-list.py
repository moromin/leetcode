# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recursive(node, prev):
            if not node:
                return prev
            next = node.next
            node.next = prev
            return recursive(next, node)
        
        return recursive(head, None)
        