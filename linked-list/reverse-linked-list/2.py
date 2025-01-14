# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        result = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return result

solution = Solution()
test = solution.reverseList(ListNode(1, ListNode(2, ListNode(4, ListNode(3)))))
print('hi')