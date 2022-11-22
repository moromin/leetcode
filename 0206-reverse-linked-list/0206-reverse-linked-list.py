# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        q = []
        while head:
            q.append(head)
            head = head.next
        N = len(q)
        for i in range(N - 1, 0, -1):
            q[i].next = q[i - 1]
        q[0].next = None
        return q[N - 1]