# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = head
        dq = deque()
        while node:
            dq.append(node)
            node = node.next
        
        i = 0
        head = dq.popleft()
        while dq:
            if i % 2 == 0:
                head.next = dq.pop()
            else:
                head.next = dq.popleft()
            head = head.next
            i += 1
        head.next = None