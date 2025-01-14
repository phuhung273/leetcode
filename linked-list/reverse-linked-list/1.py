# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode

        return prev

solution = Solution()
test = solution.reverseList(ListNode(1, ListNode(2, ListNode(4, ListNode(3)))))
print('hi')