
# type: ignore

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead = None
        length = 0
        while head != None:
            nxt = head.next
            head.next = reversedHead
            reversedHead = head
            head = nxt
            length += 1
        
        mid = length // 2
        if length % 2 == 1:
            mid += 1

        for _ in range(mid):
            nxt = reversedHead.next
            reversedHead.next = head
            head = reversedHead
            reversedHead = nxt
        return head

sol = Solution()
sol.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
sol.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
