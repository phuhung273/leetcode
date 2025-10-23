
# type: ignore

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        originalHead = head
        length = 0
        while head != None:
            head = head.next
            length += 1
        
        for _ in range(length // 2):
            originalHead = originalHead.next
        return originalHead

sol = Solution()
sol.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
sol.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
